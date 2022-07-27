with open("input") as f:
    lanternfish = f.read().split(",")

lanternfish = [int(numeric_string) for numeric_string in lanternfish]

print(lanternfish)
print(len(lanternfish))

# input_website = [3, 4, 3, 1, 2]

# Part 1
days = 1 #max days 80
max_days = 80
max_days_part_2 = 256
new_lanternfish = []

while days <= max_days:
    new_lanternfish = []
    for i in range(0, len(lanternfish)):
        if lanternfish[i] == 0:
            lanternfish[i] = 6
            new_lanternfish.append(8)

        else:
            lanternfish[i] = lanternfish[i] - 1
    for fish in new_lanternfish:
        lanternfish.append(fish)

    print("After Day ", days)
    # print(lanternfish)
    # print(new_lanternfish)
    days += 1

print("Solution Part 1:", len(lanternfish))

# Part 2 How many Lanternfish after 256 days?
# creating a new max day value

data = {}

with open("input") as f:
    array = [int(x) for x in f.readline().split(",")]

    for value in range(max(9, max(array))):
        data[value] = 0
    for element in array:
        data[element] += 1

for days in range(256):
    zeroes = data[0]
    data[0] = 0
    for index in range(1, len(data)):
        data[index-1] += data[index]
        data[index] = 0
    data[6] += zeroes
    data[8] += zeroes

sum = 0
for key in data:
    sum += data[key]

print("Solution Part 2:", sum)




