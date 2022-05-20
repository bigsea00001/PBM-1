from typing import List
from .utils.utils import Utils
from .utils.info.base import kwargs_schema


class Base_model:
    """
    """

    def __init__(self, **kwargs):
        self.utils = Utils(**kwargs)

    def params_value(self):
        return self.utils.value
