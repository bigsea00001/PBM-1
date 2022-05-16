"""
python base model's utils
"""
import os
import pymysql
from typing import List

from .info import base
from .models.database.db_model import DB_model


class Utils:
    """
    Utils for main
    """

    def __init__(self):
        self.info = base.base_info
        self._dir_check()

    def _dir_check(self) -> None:
        """
        check the directories for Util
        """
        directories: List = self.info['directories']

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)

    @classmethod
    def get_conn(cls, model: DB_model) -> pymysql.connect:
        """
        get the pymysql's connection
        """
        conn = pymysql.connect(host=model.host,
                               db=model.db_name,
                               user=model.user,
                               password=model.password,
                               port=model.port)
        return conn

    def insert_db(self, input_rows, table_info):
        table_name = table_info['table_name']
        table_scheme = table_info['scheme']
        scheme_format = tuple(table_scheme)
        values_format = ['%s' for i in range(len(table_scheme))]
        values_format = tuple(values_format)

        try:
            conn = self.get_conn(model=raw_model)  # define the model and load
            curs = conn.cursor()
            for row in input_rows:
                sql = "INSERT INTO RAW.{}".format(table_name) + \
                    "({})".format(",\n ".join(scheme_format)) + \
                    " VALUES({})".format(",\n".join(values_format))
                curs.execute(sql, row)

            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            bot.send_message(
                chat_id=chat_id,
                text=f'Stopped IARC_scraper by error occurred in inserting data \n{e}')
            conn.commit()
            conn.close()
