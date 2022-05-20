"""
python base model's utils
"""
import os
import pymysql
from typing import List, Dict

from .info import base
from .models.database import DB_model, DB_handler
from .models.pre_set import Pre_set as PS


class Utils:
    """
    Utils for main
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.base_info = base.base_info
        self.ps = PS(info=base)
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
                if kwargs_info[param]['return'] is False:
                    func = kwargs_info[param]['name']
                    eval(f'self.ps.{func}()')

                elif kwargs_info[param]['return'] is True:
                    func = kwargs_info[param]['name']
                    _return_name = kwargs_info[param]['return_name']
                    exec(f'{_return_name} = self.ps.{func}()')
                    self.value[_return_name] = eval(_return_name)
