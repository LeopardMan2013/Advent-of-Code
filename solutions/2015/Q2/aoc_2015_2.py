def get_total_area(dimensions):
    l,w,h = dimensions.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    return 2 * (l * w + l * h + w * h) + smallest_area([l,w,h])

def smallest_area(dimensions):
    dimensions.sort()
    return dimensions[0] * dimensions[1]

with open(
    #"/Users/jackmacdonald/Dev/Advent-of-Code/input/2015/day2/day2_test_input.txt", "r"
    "/Users/jackmacdonald/Dev/Advent-of-Code/input/2015/day2/day2_full_input.txt", "r"
) as input_f:
    input_lines = input_f.readlines()

part1_answer = 0
for l in input_lines:
    part1_answer += get_total_area(l)

print(f'2015 q2 part1: {part1_answer}')