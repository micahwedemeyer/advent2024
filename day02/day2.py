from functools import reduce;

def read_input():
    with open('input.txt', 'r') as input:
        return input.readlines()

def split_lines(lines):
    return [[int(x) for x in line.split()] for line in lines]

def is_safe(report):
    x,y,is_unsafe = reduce(is_safe_red, report, (None, None, False))
    return not is_unsafe

def is_safe_red(data, val):
    prev, direction, is_unsafe = data
    if is_unsafe:
        return (None, None, True)

    if prev is None:
        return (val, None, False)
    
    diff = prev - val
    if diff == 0 or abs(diff) > 3:
        return (None, None, True)

    new_direction = 1 if abs(diff) == diff else - 1

    if direction is not None and new_direction != direction:
        return (None, None, True)

    return (val, new_direction, False)

def is_safe_with_damper(report):
    for i in range(len(report)):
        sub_report = report[0:i] + report[i+1:]
        if is_safe(sub_report):
            return True

    return False

reports = split_lines(read_input())
safes = [report for report in reports if is_safe(report)]
unsafes = [report for report in reports if not is_safe(report)]
safes2 = [report for report in unsafes if is_safe_with_damper(report)]
print(len(safes) + len(safes2))