from random import choices
from typing import Tuple

import pdfkit

from exercise_template import ExerciseTemplate

EXERCISE_PLACEHOLDER = '#####'
SEED_PLACEHOLDER = '-----SEED-----'


class WorksheetSpec:
    name: str
    weights: Tuple[float, ...]
    templates: Tuple[ExerciseTemplate, ...]

    def __init__(self, name: str, template_portions: Tuple[Tuple[float, ExerciseTemplate, ], ...]) -> None:
        self.name = name
        self.weights, self.templates = zip(*template_portions)

    def generate_exercise(self) -> str:
        return choices(self.templates, self.weights)[0].generate_exercise()

    def generate_worksheet(self, current_seed: int, file_format: str = 'pdf') -> None:
        with open('worksheet_template.html', 'r') as template:
            worksheet = ''.join(
                line.replace(EXERCISE_PLACEHOLDER, self.generate_exercise()).replace(SEED_PLACEHOLDER, str(current_seed))
                for line in template
            )
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
