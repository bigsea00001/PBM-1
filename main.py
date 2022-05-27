from typing import List, overload, Dict, Union, Optional
from .utils import Utils, DB_handler, DB_model, info
#  from .utils.info.base import kwargs_schema


class BaseModel:
    """
    base_model for base coding
    """

    @overload
    def __init__(
            self,
            selenium_ops: bool,
            dir_check: bool,
            add_db: DB_model,
            db_conn: str,
            etc_info
    ): ...

    @overload
    def __init__(self): ...

    def __init__(self, **kwargs):
        self.utils = Utils(**kwargs)

    def get_value(self) -> Dict:
        """
        get parameter's value
        """
        return self.utils.value
