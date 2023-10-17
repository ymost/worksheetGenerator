from random import choices
from typing import Tuple

import pdfkit

from exercise_template import ExerciseTemplate

EXERCISE_PLACEHOLDER = '#####'
FIRST_NUMBER_PLACEHOLDER = '##1##'
OPERATOR_PLACEHOLDER = '##o##'
SECOND_NUMBER_PLACEHOLDER = '##2##'
SEED_PLACEHOLDER = '-----SEED-----'


class WorksheetSpec:
    name: str
    weights: Tuple[float, ...]
    templates: Tuple[ExerciseTemplate, ...]

    def __init__(self, name: str, template_portions: Tuple[Tuple[float, ExerciseTemplate, ], ...]) -> None:
        self.name = name
        self.weights, self.templates = zip(*template_portions)

    def generate_exercise_parts(self) -> Tuple[int, str, int]:
        return choices(self.templates, self.weights)[0].generate_exercise_parts()

    def generate_worksheet(self, current_seed: int, exercise_format: str = 'horizontal', file_format: str = 'pdf') -> None:
        if exercise_format == 'horizontal':
            with open('worksheet_template.html', 'r') as template:
                worksheet = ''.join(
                    line.replace(EXERCISE_PLACEHOLDER, '{} {} {} ='.format(*self.generate_exercise_parts())).replace(SEED_PLACEHOLDER, str(current_seed))
                    for line in template
                )
        elif exercise_format == 'vertical':
            with open('worksheet_template_vertical.html', 'r') as template:
                worksheet = ''.join(
                    line
                    .replace(FIRST_NUMBER_PLACEHOLDER, str((parts := self.generate_exercise_parts())[0]))
                    .replace(OPERATOR_PLACEHOLDER, parts[1])
                    .replace(SECOND_NUMBER_PLACEHOLDER, str(parts[2]))
                    .replace(SEED_PLACEHOLDER, str(current_seed))
                    for line in template
                )
        else:
            raise ValueError("Unknown exercise format")
        if file_format == 'pdf':
            pdfkit.from_string(
                worksheet, f'worksheet_{self.name}.pdf',
                options={
                    'page-size': 'A4',
                    'orientation': 'Portrait',
                    'margin-top': 20,
                    'log-level': 'none',
                }
            )
        elif file_format == 'html':
            with open(f'worksheet_{self.name}.html', 'w') as f:
                f.write(worksheet)
        else:
            raise ValueError("Unknown file format")
