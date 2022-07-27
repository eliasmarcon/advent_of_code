with open("input.txt") as f:
    string_nn = f.read().splitlines()

string_nn = []

vowels = ["a", "e", "i", "o", "u"]
bad_string = ["ab", "cd", "pq", "xy"]

counter_all = 0

for string in string_nn:
    zwischen_counter = 0
    counter_vowels = 0
    counter_doubels = 0
    counter_bad = 0

    for i in range(0, len(string), 1):
        if i < len(string) - 1 and string[i] == string[i + 1]:
            counter_doubels += 1

        if string[i] in vowels:
            zwischen_counter += 1
            if zwischen_counter == 3:
                counter_vowels += 1

        if i < len(string) - 1:
            if string[i: i + 2] in bad_string:
                counter_bad = 1

    if counter_vowels >= 1 and counter_doubels >= 1 and counter_bad == 0:
        counter_all += 1

print(counter_all)

# Part 2

counter_all_2 = 0

for string in string_nn:
    counter_repeat = 0
    counter_pair = 0

    for i in range(0, len(string), 1):
        if i < len(string) - 2 and string[i] == string[i + 2]:
            counter_repeat += 1

        if i < len(string) - 1:
            if string[i:i+2] in string[i+2:]:
                counter_pair += 1

    if counter_repeat >= 1 and counter_pair >= 1:
        counter_all_2 += 1

print(counter_all_2)
