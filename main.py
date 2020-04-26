from specs import SPECS

if __name__ == '__main__':
    print("Generating worksheets...")
    for spec in SPECS:
        print(f"Generating worksheet: {spec.name}")
        spec.generate_worksheet()
    print("Done")
