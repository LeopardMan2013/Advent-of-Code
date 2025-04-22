with open(
    "/Users/jackmacdonald/Dev/Advent-of-Code/input/2015/day1/day1_full_input.txt", "r"
) as input_f:
    input_lines = input_f.readlines()

floor = 0
char_pos = 1  # only needed for part 2
for line in input_lines:
    for char in line:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:  # only needed for part 2
            break  # only needed for part 2
        char_pos += 1  # only needed for part 2

# print(f"The answer is {floor}")
print(f"The answer to part 2 is {char_pos}")
