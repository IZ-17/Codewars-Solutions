from collections.abc import Callable
​
def _if(bool, func1: Callable, func2: Callable):
    if bool:
        return func1()
    return func2()