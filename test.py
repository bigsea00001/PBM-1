from typing import Tuple, overload

@overload
def foo(arg1: int, arg2: int) -> Tuple[int, int]:
    pass

@overload
def foo(arg: int) -> int:
    pass

def foo(*args):
    try:
        i, j = args
        return j, i
    except ValueError:
        assert len(args) == 1
        i = args[0]
        return i

