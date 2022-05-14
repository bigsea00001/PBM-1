"""
python base model's utils
"""
import os
from typing import List

from .info import base


class Utils:
    """
    Utils for main
    """

    def __init__(self):
        self.info = base.base_info

    def _dir_check(self) -> None:
        """
        check the directories for Util
        """
        directories: List = self.info['directories']

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)

    def do_job(self):
        """
        execute the functions that writen in base_info
        """
        functions = self.info['functions']

        for function in functions:
            eval(f'{function}')
