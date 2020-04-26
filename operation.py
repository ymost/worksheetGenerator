from enum import Enum
from operator import add, sub, mul, truediv
from typing import Callable


class Operation(Enum):
    addition = (add, '+')
    subtraction = (sub, '&#8722;')
    multiplication = (mul, '&#215;')
    division = (truediv, ':')

    def __init__(self, operation_callable: Callable[[int, int], int], symbol: str):
        self.call: Callable[[int, int], int] = operation_callable
        self.symbol: str = symbol
