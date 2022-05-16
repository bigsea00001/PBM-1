from typing import List
from utils.utils import Utils

utils = Utils()

test_row = [['dd','ddd', 'eee'], ['a', '333333', 'what ss']]
max_len = utils.DB_handler.get_max_len(rows=test_row)
print(max_len)
