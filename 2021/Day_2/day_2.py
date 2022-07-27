with open("input") as f:
    dive = f.read().splitlines()

# Part 1

forward = "forward"
down = "down"
up = "up"
sum_forward = 0
sum_up = 0
sum_down = 0

for element in dive:
    if forward in element:
        for number in element.split():
            if number.isdigit():
                temp = int(number)
                sum_forward += temp
    elif down in element:
        for number in element.split():
            if number.isdigit():
                temp = int(number)
                sum_down += temp
    elif up in element:
        for number in element.split():
            if number.isdigit():
                temp = int(number)
                sum_up += temp

print("Solution Part 1:", sum_forward * (sum_down - sum_up))

# Part 2

horizontal_position = 0
aim = 0
depth = 0

for element in dive:
    if forward in element:
        for number in element.split():
            if number.isdigit():
                temp = int(number)
                horizontal_position += temp
                depth += (aim * temp)
    elif down in element:
        for number in element.split():
            if number.isdigit():
                temp = int(number)
                aim += temp
    elif up in element:
        for number in element.split():
            if number.isdigit():
                temp = int(number)
                aim -= temp

print("Solution Part 2:", sum_forward * depth)

