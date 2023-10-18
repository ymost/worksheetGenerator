from typing import Tuple

from constraints import BaseConstraint, MAX_ITER
from operation import Operation


class ExerciseTemplate:
    operation: Operation
    operand_1_constraint: BaseConstraint
    operand_2_constraint: BaseConstraint
    result_constraint: BaseConstraint

    def __init__(self, operation: Operation, operand_1_constraint: BaseConstraint, operand_2_constraint: BaseConstraint, result_constraint: BaseConstraint) -> None:
        self.operation = operation
        self.operand_1_constraint = operand_1_constraint
        self.operand_2_constraint = operand_2_constraint
        self.result_constraint = result_constraint

    def generate_exercise_parts(self) -> Tuple[str, str, str]:
        for _ in range(MAX_ITER):
            number_1: int = self.operand_1_constraint.generate()
            number_2: int = self.operand_2_constraint.generate()
            result: int = self.operation.call(number_1, number_2)
            # Not the most efficient way, but good enough
            if self.result_constraint.test(result):
                break
        else:
            raise ValueError('Generated results are not in required range')
        return f'{number_1:,}', self.operation.symbol, f'{number_2:,}'
