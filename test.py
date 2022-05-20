from typing import Dict
k: Dict = {'a': None}

exec(f'{list(k.keys())[0]} = 2', {'__builtins__' : None}, k)
print(k)
