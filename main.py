from typing import List
from .utils.utils import Utils
from .utils.info.base import kwargs_schema


class Base_model:
    """
    base_model for base coding
    """

    def __init__(self, etc_info=None, **kwargs):
        self._etc_info = etc_info
        self.utils = Utils(etc_info=self._etc_info, **kwargs)

    def params_value(self):
        return self.utils.value
