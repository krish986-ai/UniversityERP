with open('C:/Users/sahil/Desktop/PBL_OS/UniversityERP/app.py', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if "course['faculty']" in line:
            print(f'{i}: {line.rstrip()}')