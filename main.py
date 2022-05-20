from typing import List
from .utils.utils import Utils
from .utils.info.base import kwargs_schema


class Base_model:
    """
    """

    def __init__(self, etc_info=None, **kwargs):
        self.utils = Utils(info=etc_info, **kwargs)

    def params_value(self):
        return self.utils.value
