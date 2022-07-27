with open("input") as f:
    numbers = f.read().split(",")

numbers = [int(numeric_string) for numeric_string in numbers]

turn_number = 6
spoken_numbers = []
end_turn = 2020

for number in numbers:
    spoken_numbers.append(number)


def memory(turn_number_input, end_turn_number):
    while turn_number_input < end_turn_number:

        turn_number_input += 1
        last_number = spoken_numbers[turn_number_input - 2]
        occurrences = spoken_numbers.count(spoken_numbers[turn_number_input - 2])

        if occurrences == 1:
            spoken_numbers.append(0)
        else:

            list_occurrences = [i for i in range(len(spoken_numbers)) if spoken_numbers[i] == last_number]
            last_occ = list_occurrences[len(list_occurrences) - 1]
            last_before_occ = list_occurrences[len(list_occurrences) - 2]

            difference = last_occ - last_before_occ
            spoken_numbers.append(difference)

    return spoken_numbers[-1]


print("Solution Part 1:", memory(turn_number, end_turn))

# Part 2

data = [2, 0, 1, 9, 5, 19]
dictdata = {v: k for k, v in enumerate(data[:-1])}
consider = data[-1]

for idx in range(len(data), 30000000):
    if consider in dictdata:
        next_val = (idx - 1) - dictdata[consider]
    else:
        next_val = 0

    dictdata[consider] = idx - 1
    consider = next_val

print("Solution Part 2:", next_val)
