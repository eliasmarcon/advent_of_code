import math

with open("input") as f:
    coordinates = f.read().splitlines()

print(coordinates)

coord_dict = {"N": 0, "E": 0, "S": 0, "W": 0}
cur_position = "E"

for coordinate in coordinates:
    direction = coordinate[0]
    value = coordinate[1:]

    if direction == "F":
        coord_dict[cur_position] += int(value)

    if direction == "R":
        orientation = ["N", "E", "S", "W"]
        pos_value = int(int(value) / 90)
        pos_index = (orientation.index(cur_position) + pos_value) % len(orientation)
        cur_position = orientation[pos_index]

    elif direction == "L":
        orientation = ["N", "W", "S", "E"]
        pos_value = int(int(value) / 90)
        pos_index = (orientation.index(cur_position) + pos_value) % len(orientation)
        cur_position = orientation[pos_index]

    if direction == "N":
        coord_dict[direction] += int(value)

    elif direction == "E":
        coord_dict[direction] += int(value)

    elif direction == "S":
        coord_dict[direction] += int(value)

    elif direction == "W":
        coord_dict[direction] += int(value)

print("Solution Part 1:", abs(coord_dict["N"] - coord_dict["S"]) + abs(coord_dict["W"] - coord_dict["E"]))


# Part 2

def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))


coord = {'x': 0, 'y': 0}
waypoint = {'x': 10, 'y': 1}

for line in coordinates:
    direction = line[0]
    value = line[1:]
    value = int(value)

    if direction == 'N':
        waypoint['y'] += value
    elif direction == 'S':
        waypoint['y'] -= value
    elif direction == 'E':
        waypoint['x'] += value
    elif direction == 'W':
        waypoint['x'] -= value
    elif direction == 'F':
        coord['y'] += waypoint['y'] * value
        coord['x'] += waypoint['x'] * value
    elif direction in ['L', 'R']:
        if direction == 'R':
            value = -value

        waypoint['x'], waypoint['y'] = rotate(
            (0, 0), (waypoint['x'], waypoint['y']), math.radians(value)
        )

print("Solution Part 2:", abs(coord['x']) + abs(coord['y']))

# coord_dict = {"N": 0, "E": 0, "S": 0, "W": 0}
# waypoint = {"N": 1, "E": 10, "S": 0, "W": 0}
#
# cur_position_x = "E"
# cur_position_y = "N"
#
# for coordinate in coordinates:
#     direction = coordinate[0]
#     value = coordinate[1:]
#
#     if direction == "F":
#         coord_dict[cur_position_x] += int(value) * waypoint[cur_position_x]
#         coord_dict[cur_position_y] += int(value) * waypoint[cur_position_y]
#
#     elif direction == "R":
#         orientation = ["N", "E", "S", "W"]
#         pos_value = int(int(value) / 90)
#
#         # X Coordinate
#         pos_index_x = (orientation.index(cur_position_x) + pos_value) % len(orientation)
#         new_position_x = orientation[pos_index_x]
#
#         # Y Coordinate
#         pos_index_y = (orientation.index(cur_position_y) + pos_value) % len(orientation)
#         new_position_y = orientation[pos_index_y]
#
#         temp_x = waypoint[cur_position_x]
#         temp_y = waypoint[cur_position_y]
#
#         waypoint[new_position_x] = temp_x
#         waypoint[new_position_y] = temp_y
#         waypoint[cur_position_y] = 0
#         cur_position_x = new_position_x
#         cur_position_y = new_position_y
#
#     elif direction == "L":
#         orientation = ["N", "W", "S", "E"]
#         pos_value = int(int(value) / 90)
#
#         # Y Coordinate
#         pos_index_y = (orientation.index(cur_position_y) + pos_value) % len(orientation)
#         new_position_y = orientation[pos_index_y]
#
#         # X Coordinate
#         pos_index_x = (orientation.index(cur_position_x) + pos_value) % len(orientation)
#         new_position_x = orientation[pos_index_x]
#
#         temp_y = waypoint[cur_position_y]
#         temp_x = waypoint[cur_position_x]
#
#         waypoint[new_position_y] = temp_y
#         waypoint[new_position_x] = temp_x
#         waypoint[cur_position_x] = 0
#         cur_position_y = new_position_y
#         cur_position_x = new_position_x
#
#     elif direction == "N":
#         waypoint[direction] += int(value)
#
#     elif direction == "E":
#         waypoint[direction] += int(value)
#
#     elif direction == "S":
#         waypoint[direction] += int(value)
#
#     elif direction == "W":
#         waypoint[direction] += int(value)
#
#     print(coord_dict)
#
# print("Solution Part 2:", abs(coord_dict["N"] - coord_dict["S"]) + abs(coord_dict["E"] - coord_dict["W"]))
#
#
