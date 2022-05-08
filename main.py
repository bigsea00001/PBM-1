from typing import List
from utils.utils import Utils

utils = Utils()

temp: List = [['aa', 'bbbb', 'dddddd'],
              ['a', 'dddddddddd', 'iiiiiii'],
              ['dddddddddddddd', 'dd', 'ddddddddddddddddd']]

elements_max_length = utils.max_length_check(rows=temp)
print(elements_max_length)
