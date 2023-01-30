from abc import ABC, abstractmethod
from random import randint
from typing import Union

MAX_ITER = 10000


class BaseConstraint(ABC):
    @abstractmethod
    def test(self, num: int) -> bool:
        pass

    @abstractmethod
    def generate(self) -> int:
        pass


class NoConstraint(BaseConstraint):
    def test(self, num: int) -> bool:
        return True

    def generate(self) -> int:
        raise NotImplementedError()


class InRange(BaseConstraint):
    def __init__(self, range_start: int, range_end: int) -> None:
        """
        Range is inclusive
        """
        assert range_start <= range_end
        self.range_start: int = range_start
        self.range_end: int = range_end

    def test(self, num: int) -> bool:
        return self.range_start <= num <= self.range_end

    def generate(self) -> int:
        return randint(self.range_start, self.range_end)


class MultipleOf(BaseConstraint):
    def __init__(self, multiplier: Union[int, float], other_constraint: BaseConstraint = NoConstraint()) -> None:
        self.multiplier = multiplier
        self.other_constraint: BaseConstraint = other_constraint

    def test(self, num: int) -> bool:
        quotient, remainder = divmod(num, self.multiplier)
        return remainder == 0 and self.other_constraint.test(quotient)

    def generate(self) -> int:
        return self.multiplier * self.other_constraint.generate()


class Even(BaseConstraint):
    def __init__(self, other_constraint: BaseConstraint) -> None:
        self.other_constraint: BaseConstraint = other_constraint

    def test(self, num: int) -> bool:
        return self.other_constraint.test(num) and num % 2 == 0

    def generate(self) -> int:
        for _ in range(MAX_ITER):
            generated = self.other_constraint.generate()
            if generated % 2 == 0:
                return generated
        raise ValueError('No even number found')
