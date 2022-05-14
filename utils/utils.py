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
        pass

    @classmethod
    def _dir_check(cls) -> None:
        """
        check the directories for Util
        """
        directories: List = base.base_info['directories']

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)
