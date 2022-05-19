"""
python base model's utils
"""
import os
import pymysql
from typing import List

from .info import base
from .models.database import DB_model, DB_handler


class Utils:
    """
    Utils for main
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.base_info = base.base_info
        self.parameter_checK()

    def parameter_checK(self):
        kwargs_info = base.kwargs_info
        inputed_param = list(self.kwargs.keys())
        defined_param = list(kwargs_info.keys())

        selected_params: List = set(inputed_param) & set(defined_param)

        for params in selected_params:
            if kwargs_info[params]['type'] == 'func':
                if self.kwargs[params] is True:
                    func = kwargs_info[params]['name']
                    eval(f'self.{func}()')

        return selected_params

    def _dir_check(self) -> None:
        """
        check the directories for Util
        """
        directories: List = self.base_info['dirs']

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)
