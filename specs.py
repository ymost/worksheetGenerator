from typing import Tuple

from constraints import InRange, Even, NoConstraint
from exercise_template import ExerciseTemplate
from operation import Operation
from worksheet_spec import WorksheetSpec

SPECS: Tuple[WorksheetSpec, ...] = (
    WorksheetSpec('ages 5-6', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 15), InRange(0, 15), InRange(0, 30))),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 10), InRange(0, 10), InRange(0, 10))),
        (0.4, ExerciseTemplate(Operation.subtraction, InRange(0, 9), InRange(0, 10), InRange(-9, -1))),
        (0.4, ExerciseTemplate(Operation.multiplication, InRange(0, 5), InRange(0, 5), InRange(0, 25))),
        (0.2, ExerciseTemplate(Operation.division, Even(InRange(0, 16)), InRange(2, 2), NoConstraint()))
    )),
    WorksheetSpec('ages 3-4', (
        (1, ExerciseTemplate(Operation.addition, InRange(0, 9), InRange(0, 9), InRange(0, 18))),
        (1, ExerciseTemplate(Operation.subtraction, InRange(0, 9), InRange(0, 9), InRange(0, 9))),
    )),
)