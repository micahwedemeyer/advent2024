def read_input():
    with open('input.txt', 'r') as input:
        return input.readlines()

def get_rules(raw_lines):
    return [line.strip() for line in raw_lines if "|" in line]

def get_updates(raw_lines):
    return [line.strip().split(",") for line in raw_lines if "," in line]

def gen_possible_rules(update, idx):
    return [f"{update[idx]}|{update[j]}" for j in range(idx)]

def is_valid(update, rules):
    possible_rules = [r for i in range(1, len(update)) for r in gen_possible_rules(update, i)]
    for pr in possible_rules:
        if pr in rules:
            return False
    return True

def is_valid_at_index(update, idx, rules):
    for pr in gen_possible_rules(update, idx):
        if pr in rules:
            return False
    return True

### Idea: We need to find possible_rules for a specific index, as we move the elements from right to left. It's not a test of "is this update valid?"
### but instead, "is this particular placement for this number valid within this update?" The entire update may still be invalid, but we have to
### know when we're done moving an element to the left.

def fix_invalid(update, rules):
    tester = update.copy()
    if is_valid(tester, rules):
        return tester

    i = len(tester) - 1
    while i >= 0:
        tester = find_valid_spot(tester, i, rules)
        if is_valid_at_index(tester, i, rules):
            i = i - 1

    return tester

def find_valid_spot(update, idx, rules):
    tester = update.copy()
    if is_valid_at_index(tester, idx, rules):
        return tester

    for i in range(idx, 0, -1):
        tester = tester[:i-1] + [tester[i]] + [tester[i-1]] + tester[i+1:]
        possible_rules = gen_possible_rules(tester, i)
        if is_valid_at_index(tester, i, rules):
            return tester


lines = read_input()
rules = get_rules(lines)
updates = get_updates(lines)

valids = [update for update in updates if is_valid(update, rules)]
invalids = [update for update in updates if not is_valid(update, rules)]
fixed = [fix_invalid(update, rules) for update in invalids]

# for update in invalids:
#     print(f"inv: {update}")
#     print(f"val: {fix_invalid(update, rules)}")
#    t = find_valid_spot(update, )

# ex = invalids[0]
# ex2 = find_valid_spot(ex, 2, rules)
# print(ex2)

# print(ex)
# print(fix_invalid(ex, rules))

middles = [int(update[divmod(len(update), 2)[0]]) for update in fixed]

# print(valids)
print(middles)
print(sum(middles))

    # print("update:" + ",".join(update))
    # for i in range(1, len(update)):
    #     possible_rules = [f"{update[i]}|{update[j]}" for j in range(i)]
    #     print(possible_rules)


# good = "16|65" in rules
# print(good)