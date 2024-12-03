def read_input():
    with open('input.txt', 'r') as input:
        return input.readlines()

def split_input(lines):
    pairs = [tuple([int(x) for x in line.split()]) for line in lines]
    dual_lists = list(zip(*pairs))
    return (list(dual_lists[0]), list(dual_lists[1]))



def calc_diff(dual_lists):
    sorted1 = dual_lists[0]
    sorted1.sort()
    sorted2 = dual_lists[1]
    sorted2.sort()

    sum = 0
    for idx, item1 in enumerate(sorted1):
        item2 = sorted2[idx]
        sum += abs(item1 - item2)

    return sum

def calc_similarity(dual_lists):
    return sum([x * len([y for y in dual_lists[1] if x == y]) for x in dual_lists[0]])


lines = read_input()
dual_lists = split_input(lines)
sims = calc_similarity(dual_lists)
print(sims)