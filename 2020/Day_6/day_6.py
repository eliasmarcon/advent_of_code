import collections

with open("input") as f:
    answers_unsorted = f.read().split("\n\n")

# print(answers_unsorted)

answers_sorted = []

for line in answers_unsorted:
    line = line.replace("\n", " ")
    answers_sorted.append(line)

# print(answers_sorted)

# Part 1
counter_answers = 0

for answer in answers_sorted:
    unique_letters = []
    for char in answer:
        if char not in unique_letters and char != " ":
            unique_letters.append(char)
            counter_answers += 1

print("Solution Part 1:", counter_answers)

# Part 2
counter_answers = 0

for answer in answers_sorted:
    group = answer.split(" ")
    group_elements = []

    for element in group:
        for char in element:
            group_elements.append(char)

    occurrences = collections.Counter(group_elements)
    for element in occurrences:

        if occurrences[element] >= len(group):
            counter_answers += 1

print("Solution Part 2:", counter_answers)
