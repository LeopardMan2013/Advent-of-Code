with open(
    "/Users/hamish.macdonald/Dev/Jack/Advent-of-Code/2015/Q1/input.txt", "r"
) as input_f:
    input_lines = input_f.readlines()

floor = 0
for line in input_lines:
    for char in line:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

print(f"The answer is {floor}")
