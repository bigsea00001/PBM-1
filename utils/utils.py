"""
python base model's utils
"""
import os
import pymysql
from typing import List

from .info import base
from .models.database.db_utils import DB_model, DB_handler


class Utils:
    """
    Utils for main
    """

    def __init__(self):
        self.base_info= base.base_info
        self.DB_handler = DB_handler()
        self.DB_model = DB_model

    def _dir_check(self) -> None:
        """
        check the directories for Util
        """
        directories: List = self.info['directories']

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)

