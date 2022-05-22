import os
from typing import List, Dict, Type


class Pre_set:
    def __init__(self, info):
        self.info = info

    def _dir_check(self) -> None:
        directories = self.info.base_info['dirs']

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)

    def _selenium_options_config(self):
        from selenium import webdriver

        pre_options = self.info.selenium_info['options']
        pre_experi_options = self.info.selenium_info['prefs']

        options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        for pre_option in pre_options:
            options.add_argument(pre_option)

        options.add_experimental_option('prefs', pre_experi_options)

        return options

    @classmethod
    def _add_db_model(cls, model):
        """
        create_db_model and save to json
        """
        import json

        model_json = {
            'host': model.host,
            'db_name': model.db_name,
            'user': model.user,
            'password': model.password,
            'port': model.port,
        }

        file_path = 'Data/model/database_models.json'
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as create_file:
                json_data = {'databases': {}}
                json.dump(json_data, create_file, indent=4)

        with open(file_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            json_data['databases'][model.db_name] = model_json

        with open(file_path, 'w', encoding='utf-8') as out_file:
            json.dump(json_data, out_file, indent=4)

    def _get_conn(self, db_name):
        import json
        import pymysql

        file_path = 'Data/model/database_models.json'
        with open(file_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        host = json_data[db_name]['host']
        user = json_data[db_name]['user']
        password = json_data[db_name]['password']
        port = json_data[db_name]['port']

        conn = pymysql.connect(host = host,
                               db=db_name,
                               user=user,
                               password=password,
                               port=port)

        return conn
