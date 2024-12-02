def reportSafe(report):
    i1 = report[0]
    i2 = report[1]
    if (i1 == i2) or (abs(i1 - i2) > 3):
        return False
    inc_or_dec = ''
    if i1 > i2:
        inc_or_dec = 'dec'
    else:
        inc_or_dec = 'inc'

    # print(f"i1: {i1} i2: {i2} inc_or_dec: {inc_or_dec}")

    for i in range(2, len(report)):
        i1 = i2
        i2 = report[i]
        # print(f"i1: {i1} i2: {i2}")
        if (inc_or_dec == 'dec' and i1 < i2) or ((i1 == i2) or (abs(i1 - i2) > 3)):
            return False
        elif (inc_or_dec == 'inc' and i1 > i2) or ((i1 == i2) or (abs(i1 - i2) > 3)):
            return False
    return True


with open(
    #"/Users/jackmacdonald/Dev/Advent-of-Code/input/2024/day2/day2_test_input.txt", "r"
    "/Users/jackmacdonald/Dev/Advent-of-Code/input/2024/day2/day2_full_input.txt", "r"
) as input_f:
    input_lines = input_f.readlines()

p1_ans = 0
for l in input_lines:
    l = [int(x) for x in l.strip().split(" ")]
    reportSafe(l)
    if reportSafe(l):
        p1_ans += 1

print(f"Part 1: {p1_ans}")
