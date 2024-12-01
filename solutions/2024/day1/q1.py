with open(
    #"/Users/jackmacdonald/Dev/Advent-of-Code/input/2024/day1/day1_test_input.txt", "r"
    "/Users/jackmacdonald/Dev/Advent-of-Code/input/2024/day1/day1_full_input.txt", "r"
) as input_f:
    input_lines = input_f.readlines()

l1 = []
l2 = []
for l in input_lines:
    l = l.strip()
    chars = l.split("   ")
    l1.append(int(chars[0]))
    l2.append(int(chars[1]))

l1.sort()
l2.sort()
p1_ans = 0

for i in range(len(l1)):
    p1_ans += abs(l1[i] - l2[i])

print(p1_ans)
