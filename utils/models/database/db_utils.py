from typing import Union, List, Dict
import pymysql
import json


class DB_model:
    def __init__(self, host=None, db_name=None, user=None, password=None, port=None):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.port = port


class DB_handler:
    def __init__(self):
        pass

    @classmethod
    def get_max_len(cls, rows):
        """
        get max length from List that 2 dimension
        """
        _return_row: List[None] = [1 for i in range(len(rows[0]))]

        for _, row in enumerate(rows):
            for idx_each, each in enumerate(row):
                if each is None:
                    temp_len = 4
                else:
                    temp_len = len(each)
                if temp_len > _return_row[idx_each]:
                    _return_row[idx_each] = temp_len

        return _return_row

    def insert_db(self, input_rows, table_info, conn):
        table_name = table_info['table_name']
        table_scheme = table_info['scheme']
        scheme_format = tuple(table_scheme)
        values_format = ['%s' for i in range(len(table_scheme))]
        values_format = tuple(values_format)

        try:
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
            conn.commit()
            conn.close()
