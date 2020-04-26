from random import choices
from typing import Tuple

import pdfkit

from exercise_template import ExerciseTemplate

EXERCISE_PLACEHOLDER = '#####'


class WorksheetSpec:
    name: str
    weights: Tuple[float, ...]
    templates: Tuple[ExerciseTemplate, ...]

    def __init__(self, name: str, template_portions: Tuple[Tuple[float, ExerciseTemplate, ], ...]) -> None:
        self.name = name
        self.weights, self.templates = zip(*template_portions)

    def generate_exercise(self) -> str:
        return choices(self.templates, self.weights)[0].generate_exercise()

    def generate_worksheet(self) -> None:
        with open('worksheet_template.html', 'r') as template:
            worksheet = ''.join(line.replace(EXERCISE_PLACEHOLDER, self.generate_exercise()) for line in template)
        pdfkit.from_string(
            worksheet, f'worksheet_{self.name}.pdf',
            options={
                'page-size': 'A4',
                'orientation': 'Portrait',
                'margin-top': 20,
                'log-level': 'none',
            }
        )
