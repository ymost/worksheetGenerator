from typing import Tuple

from constraints import InRange, NoConstraint, MultipleOf
from exercise_template import ExerciseTemplate
from operation import Operation
from worksheet_spec import WorksheetSpec

SPECS: Tuple[WorksheetSpec, ...] = (
    WorksheetSpec('ages 5-6', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 15), InRange(0, 15), NoConstraint())),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 15), InRange(0, 10), InRange(0, 15))),
        (0.4, ExerciseTemplate(Operation.addition, MultipleOf(10, InRange(0, 10)), MultipleOf(10, InRange(0, 10)), NoConstraint())),
        (0.4, ExerciseTemplate(Operation.subtraction, MultipleOf(10, InRange(0, 11)), MultipleOf(10, InRange(0, 10)), MultipleOf(10, InRange(0, 11)))),
        (0.4, ExerciseTemplate(Operation.multiplication, InRange(0, 6), InRange(0, 6), NoConstraint())),
        (0.2, ExerciseTemplate(Operation.division, InRange(0, 30), InRange(2, 2), NoConstraint()))
    )),
    WorksheetSpec('ages 8-9', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 1000), InRange(0, 1000), InRange(0, 2000))),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 1000), InRange(0, 1000), InRange(0, 2000))),
        (0.4, ExerciseTemplate(Operation.multiplication, InRange(0, 20), InRange(0, 20), NoConstraint())),
        (0.2, ExerciseTemplate(Operation.division, InRange(0, 50), InRange(1, 10), MultipleOf(0.25)))
    )),
    WorksheetSpec('ages 3-4', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 10), InRange(0, 10), InRange(0, 20))),
        (1, ExerciseTemplate(Operation.addition, InRange(6, 9), InRange(6, 9), InRange(12, 18))),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 9), InRange(0, 9), InRange(0, 9))),
    )),
)
