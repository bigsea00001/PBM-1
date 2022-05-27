import os
from ..database import DB_model
from typing import List, Dict, Type


class Pre_set:
    def __init__(self, info, etc_info = None):
        self.info = info
        self.etc_info = etc_info

    def _dir_check(self) -> None:
        directories = self.info.base_info["dirs"]

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)

    def _selenium_options_config(self):
        from selenium import webdriver

        pre_options = self.info.selenium_info["options"]
        pre_experi_options = self.info.selenium_info["prefs"]

        options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        for pre_option in pre_options:
            options.add_argument(pre_option)

        options.add_experimental_option("prefs", pre_experi_options)

        return options

    @classmethod
    def _add_db_model(cls, db_info):
        """
        create_db_model and save to json
        """
        import json

        file_path = "Data/model/database_models.json"

        if isinstance(db_info, DB_model):
            model_info = {
                "host": db_info.host,
                "db_name": db_info.db_name,
                "user": db_info.user,
                "password": db_info.password,
                "port": db_info.port,
            }

            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as create_file:
                    json_data = {"databases": {}}
                    json.dump(json_data, create_file, indent=4)

            with open(file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
                json_data["databases"][db_info.db_name] = model_info

            with open(file_path, "w", encoding="utf-8") as out_file:
                json.dump(json_data, out_file, indent=4)

        elif isinstance(db_info, Dict):
            model_dict = {
                'host': db_info['host'],
                'db_name': db_info['db_name'],
                'user': db_info['user'],
                'password': db_info['password'],
                'port': db_info['port']
            }

            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as create_file:
                    json_data = {"databases": {}}
                    json.dump(json_data, create_file, indent=4)

            with open(file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
                json_data["databases"][model_dict['db_name']] = model_dict

            with open(file_path, "w", encoding="utf-8") as out_file:
                json.dump(json_data, out_file, indent=4)


    def _get_conn(self, db_name):
        import json
        import pymysql

        if self.etc_info:
            host = self.etc_info.database[db_name]['host']
            user = self.etc_info.database[db_name]['user']
            password = self.etc_info.database[db_name]['password']
            port = self.etc_info.database[db_name]['port']

            conn = pymysql.connect(
                host=host, db=db_name, user=user, password=password, port=port
            )

        else:
            file_path = "Data/model/database_models.json"
            with open(file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)

            host = json_data[db_name]["host"]
            user = json_data[db_name]["user"]
            password = json_data[db_name]["password"]
            port = json_data[db_name]["port"]

            conn = pymysql.connect(
                host=host, db=db_name, user=user, password=password, port=port
            )

        return conn
