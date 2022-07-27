with open("input") as f:
    numbers = f.read().splitlines()

no_number = []
found = False
numerator = 0
preamble = 25

while not found and numerator < len(numbers):

    preamble_numbers = numbers[numerator:numerator + preamble]
    current_number = int(numbers[numerator + preamble])
    compare_number = []

    for first in preamble_numbers:
        first = int(first)

        for second in preamble_numbers:
            second = int(second)
            compare_number.append(first + second)

    if current_number not in compare_number:
        no_number = current_number
        found = True

    numerator += 1


print("Solution Part 1:", no_number)

# Part 2
value_to_find = no_number
encryption_weakness = 0

for beginning in range(0, len(numbers)):
    adding_up = 0

    for end in range(beginning, len(numbers)):
        adding_up += int(numbers[end])

        if adding_up > value_to_find:
            break
        if adding_up == value_to_find:
            range_numbers = [int(numeric_string) for numeric_string in numbers[beginning:end]]
            min_number = min(range_numbers)
            max_number = max(range_numbers)
            encryption_weakness = max_number + min_number
            break
    if encryption_weakness > 0:
        break

print("Solution Part 2:", encryption_weakness)
