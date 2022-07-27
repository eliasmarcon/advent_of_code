with open("input") as f:
    passwords = f.read().splitlines()


min_Number = []
max_Number = []
character = []
password_array = []

for password in passwords:
    first, second = password.split("-")
    min_Number.append(first)

    third, four = second.split(" ", 1)
    max_Number.append(third)

    five, six = four.split(":")
    character.append(five)
    six = six.replace(" ", "")
    password_array.append(six)

min_Number = [int(numeric_string) for numeric_string in min_Number]
max_Number = [int(numeric_string) for numeric_string in max_Number]

print(passwords)
print(min_Number)
print(max_Number)
print(character)
print(password_array)

valid = 0

for i in range(0, len(password_array)):
    if character[i] in password_array[i]:
        characters = password_array[i].count(character[i])
        if min_Number[i] <= characters <= max_Number[i]:
            valid += 1

print("Solution Part 1:", valid)


# Part 2

valid_pt = 0

# Because Toboggan doesnt have a concept of index 0, 1 is in our array 0 because its the first position in the array
min_Number = [x - 1 for x in min_Number]
max_Number = [x - 1 for x in max_Number]

for i in range(0, len(password_array)):
    if character[i] in password_array[i]:
        password = password_array[i]
        if password[min_Number[i]] == character[i] and password[max_Number[i]] != character[i] or password[min_Number[i]] != character[i] and password[max_Number[i]] == character[i]:
            valid_pt += 1

print("Solution Part 2:", valid_pt)







