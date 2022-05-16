from typing import Union, List
import pymysql


class DB_model:
    def __init__(self, host, db_name, user, password, port):
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
        _return_row: List[None] = [None for i in range(len(rows[0]))]
        elements_row: List[int] = [1 for i in rows[0]]

        for _, row in enumerate(rows):
            for idx_each, each in enumerate(row):
                if len(each) > elements_row[idx_each]:
                    _return_row[idx_each] = len(each)

        return _return_row

    @classmethod
    def get_conn(cls, model: DB_model = None) -> Union[None, pymysql.connect]:
        if model is None:
            return None

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
