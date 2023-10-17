from typing import Tuple

from constraints import InRange, NoConstraint, MultipleOf
from exercise_template import ExerciseTemplate
from operation import Operation
from worksheet_spec import WorksheetSpec

SPECS: Tuple[WorksheetSpec, ...] = (
    WorksheetSpec('ages 5-6', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 500), InRange(0, 500), NoConstraint())),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 50), InRange(0, 25), InRange(0, 50))),
        (0.1, ExerciseTemplate(Operation.addition, MultipleOf(10, InRange(0, 20)), MultipleOf(10, InRange(0, 20)), NoConstraint())),
        (0.1, ExerciseTemplate(
            Operation.subtraction, MultipleOf(10, InRange(0, 20)), MultipleOf(10, InRange(0, 10)), MultipleOf(10, InRange(0, 20))
        )),
        (0.4, ExerciseTemplate(Operation.multiplication, InRange(0, 10), InRange(0, 10), NoConstraint())),
        (0.4, ExerciseTemplate(Operation.division, InRange(0, 30), InRange(1, 5), MultipleOf(1))),
    )),
    WorksheetSpec('ages 8-9', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 10000), InRange(0, 10000), NoConstraint())),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 10000), InRange(0, 10000), InRange(0, 20000))),
        (0.4, ExerciseTemplate(Operation.multiplication, InRange(0, 100), InRange(0, 100), NoConstraint())),
        (0.2, ExerciseTemplate(Operation.division, InRange(0, 50), InRange(1, 10), MultipleOf(0.25))),
    )),
    WorksheetSpec('ages 3-4', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 10), InRange(0, 10), InRange(0, 20))),
        (1, ExerciseTemplate(Operation.addition, InRange(6, 9), InRange(6, 9), InRange(12, 18))),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 9), InRange(0, 9), InRange(0, 9))),
    )),
)
