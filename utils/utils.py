"""
python base model's utils
"""
import os
import pymysql
from typing import List, Dict

from .info import base
from .models import Pre_set, DB_handler, DB_model


class Utils:
    """
    Utils for main
    """

    def __init__(self, etc_info=None, **kwargs):
        self.kwargs = kwargs
        self.base_info = base.base_info
        self.etc_info = etc_info
        self.pre_set = Pre_set(info=base)
        self.value: Dict = {}
        self._parameter_check()

        self.db_handler = DB_handler()

    def _parameter_check(self):
        kwargs_info = base.kwargs_info
        inputed_param = list(self.kwargs.keys())
        defined_param = list(kwargs_info.keys())
        selected_params: List = set(inputed_param) & set(defined_param)

        if "db_conn" in selected_params:
            func = kwargs_info["db_conn"]["func"]
            _return_name = kwargs_info["db_conn"]["_return"]
            exec(f"{_return_name} = self.pre_set.{func}(self.kwargs['db_conn'])")
            self.value[_return_name] = eval(_return_name)
            selected_params.remove("db_conn")

        for param in selected_params:
            if kwargs_info[param]["type"] == "func" and self.kwargs[param] is True:
                if kwargs_info[param]["_return"] is None:
                    func = kwargs_info[param]["func"]
                    eval(f"self.pre_set.{func}()")
                elif not kwargs_info[param]["_return"] is None:
                    func = kwargs_info[param]["func"]
                    _return_name = kwargs_info[param]["_return"]
                    exec(f"{_return_name} = self.pre_set.{func}()")
                    self.value[_return_name] = eval(_return_name)

    def _etc_info_check(self):
        _info = self.etc_info
        _return_data: Dict = {}

        if self.etc_info is None:
            _return_data = None

        elif isinstance(self.etc_info, Dict):
            # database
            _info: Dict = _info
            _keys = _info.keys()
            table_list = _info.database['use_table']
