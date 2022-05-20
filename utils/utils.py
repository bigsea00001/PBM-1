"""
python base model's utils
"""
import os
import pymysql
from typing import List, Dict

from .info import base
from .models import CustomLogger, Pre_set, DB_handler, DB_model


class Utils:
    """
    Utils for main
    """

    def __init__(self, etc_info, **kwargs):
        self.kwargs = kwargs
        self.base_info = base.base_info
        self.etc_info = etc_info
        self.pre_set= Pre_set(info=base)
        self.logger = CustomLogger().config()
        self.db_handler = DB_handler()
        self.value: Dict = {}
        self.parameter_check()

    def parameter_check(self):
        kwargs_info = base.kwargs_info
        inputed_param = list(self.kwargs.keys())
        defined_param = list(kwargs_info.keys())
        selected_params: List = set(inputed_param) & set(defined_param)

        for param in selected_params:
            if (kwargs_info[param]['type'] == 'func' and
                    self.kwargs[param] is True):
                if kwargs_info[param]['_return'] is None:
                    func = kwargs_info[param]['func']
                    eval(f'self.pre_set.{func}()')

                elif not kwargs_info[param]['_return'] is None:
                    func = kwargs_info[param]['func']
                    _return_name = kwargs_info[param]['_return']
                    exec(f'{_return_name} = self.pre_set.{func}()')
                    self.value[_return_name] = eval(_return_name)

            elif kwargs_info[param]['type'] == 'DB_model':
                func = kwargs_info[param]['func']
                db_model = self.kwargs[param]
                eval(f'self.pre_set.{func}(db_model)')
