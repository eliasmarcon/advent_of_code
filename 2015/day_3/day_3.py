with open("input.txt") as f:
    moves = f.read()

array = []
x = 0
y = 0

starting_point = (x, y)
array.append(starting_point)

for move in moves:
    if move == "^":
        y += 1
    elif move == "v":
        y -= 1
    elif move == ">":
        x += 1
    elif move == "<":
        x -= 1
    point = (x, y)

    if point not in array:
        array.append(point)

print(len(array))

# Part 2

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0

santa_array = []
robo_array = []

starting_point = (santa_x, santa_y)
santa_array.append(starting_point)

for move_santa in range(0, len(moves), 2):
    if moves[move_santa] == "^":
        santa_y += 1
    elif moves[move_santa] == "v":
        santa_y -= 1
    elif moves[move_santa] == ">":
        santa_x += 1
    elif moves[move_santa] == "<":
        santa_x -= 1
    point = (santa_x, santa_y)

    if point not in santa_array:
        santa_array.append(point)

for move_robo in range(1, len(moves), 2):
    if moves[move_robo] == "^":
        robo_y += 1
    elif moves[move_robo] == "v":
        robo_y -= 1
    elif moves[move_robo] == ">":
        robo_x += 1
    elif moves[move_robo] == "<":
        robo_x -= 1
    point = (robo_x, robo_y)

    if point not in robo_array:
        robo_array.append(point)

print(santa_array)
print(robo_array)

for move in santa_array:
    if move not in robo_array:
        robo_array.append(move)

print(robo_array)
print(len(robo_array))
