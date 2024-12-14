import re
from io import StringIO

matcher = r"mul\((\d{1,3}),(\d{1,3})\)"

def read_input():
    with open('input.txt', 'r') as input:
        return input.read()

def mul(x,y):
    return int(x) * int(y)

def do_dont_swapper(raw):
    input_buffer = StringIO(raw)
    good_buffer = StringIO()
    bad_buffer = StringIO()
    trigger_buffer = ""
    current_buffer = good_buffer

    character = input_buffer.read(1)
    while character:
        current_buffer.write(character)
        trigger_buffer += character

        if trigger_buffer == "do()":
            current_buffer = good_buffer
            trigger_buffer = ""
        elif trigger_buffer == "don't()":
            current_buffer = bad_buffer
            trigger_buffer = ""
        
        if not "do()".startswith(trigger_buffer) and not "don't()".startswith(trigger_buffer):
            trigger_buffer = ""

        character = input_buffer.read(1)

    return good_buffer.getvalue()


    



raw = read_input()
good = do_dont_swapper(raw)
s = sum([mul(*match) for match in re.findall(matcher, good)])
print(s)