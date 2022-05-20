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

        options: webdriver.ChromeOption = webdriver.ChromeOptions()
        for pre_option in pre_options:
            options.add_argument(pre_option)

        options.add_experimental_option('prefs', pre_experi_options)

        return options


    def _create_db_model(self, db_model):
        """
        create_db_model and save to json
        """
        import json

        model = db_model

        model_json= {
            'host' : model.host,
            'db_name': model.db_name,
            'user': model.user,
            'password': model.password,
            'port': model.port
        }

        with open('Data/model/Database.json', 'w') as json_file:
            json.dump(model_json, json_file, indent=6)
            json_file.close()
