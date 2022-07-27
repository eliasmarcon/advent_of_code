with open("input") as f:
    temp = f.read().splitlines()

output = []

for line in temp:
    temp_input, temp_output = line.split(" | ")

    temp_output_2 = temp_output.split(" ")
    for x in temp_output_2:
        output.append(x)

counter = 0
list_of_digits = [2, 3, 4, 7]

for x in output:
    if len(x) in list_of_digits:
        counter += 1

print("Solution Part 1:", counter)


# Part 2

def part2(s: str) -> int:
    lines = s.splitlines()

    total = 0

    for line in lines:
        start, end = line.split(" | ")
        end_parts = [''.join(sorted(s)) for s in end.split()]
        digits = {*start.split(), *end_parts}
        digits = {''.join(sorted(part)) for part in digits}

        num_to_s = {}

        num_to_s[1], = (s for s in digits if len(s) == 2)
        num_to_s[7], = (s for s in digits if len(s) == 3)
        num_to_s[4], = (s for s in digits if len(s) == 4)
        num_to_s[8], = (s for s in digits if len(s) == 7)
        len6 = {s for s in digits if len(s) == 6}

        num_to_s[6], = (s for s in len6 if len(set(s) & set(num_to_s[1])) == 1)
        num_to_s[9], = (s for s in len6 if len(set(s) & set(num_to_s[4])) == 4)
        num_to_s[0], = len6 - {num_to_s[6], num_to_s[9]}

        len5 = {s for s in digits if len(s) == 5}

        num_to_s[5], = (s for s in len5 if len(set(s) & set(num_to_s[6])) == 5)
        num_to_s[3], = (s for s in len5 if len(set(s) & set(num_to_s[1])) == 2)
        num_to_s[2], = len5 - {num_to_s[5], num_to_s[3]}

        s_to_num = {v: k for k, v in num_to_s.items()}

        total += sum(10 ** (3 - i) * s_to_num[end_parts[i]] for i in range(4))

    return total


with open("input") as f:
    temo = f.read()

print("Solution Part 2:", part2(temo))








