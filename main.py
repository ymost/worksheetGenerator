import sys
from random import randrange, seed

from specs import SPECS

SEED = None


if __name__ == '__main__':
    if SEED is None:
        print("Generating seed")
        current_seed = randrange(sys.maxsize)
    else:
        print("Using provided seed")
        current_seed = SEED
    print(f"Using seed: {current_seed}")
    seed(current_seed)
    print("Generating worksheets...")
    for spec in SPECS:
        print(f"Generating worksheet: {spec.name}")
        spec.generate_worksheet(current_seed)
    print("Done")
