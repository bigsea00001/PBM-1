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

    def get_model(self, _db_name):
        file_path = 'Data/model/database_models.json'
        with open(file_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        #  db_name = json_data[self.get_name]['db_name']
        db_name = _db_name
        host = json_data[db_name]['host']
        user = json_data[db_name]['user']
        password = json_data[db_name]['password']
        port = json_data[db_name]['port']
        _model = DB_model(host=host, db_name=db_name,
                          user=user, password=password, port=port)

        return _model


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

    @classmethod
    def get_conn(cls, db_name: str = None) -> Union[None, pymysql.connect]:
        if db_name is None:
            return None

        model = DB_model().get_model(_db_name=db_name)

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
            conn = self.get_conn(model=None)  # define the model and load
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
