with open("input") as file:

    commands = file.readline().split(", ")


## PART 1 ----------------------------------------------------------------------------------------------------------
def calculate_distance(instructions):
    
    x, y = 0, 0  # Starting point
    direction = 0  # 0: North, 1: East, 2: South, 3: West
    
    for instruction in instructions:

        turn = instruction[0]
        steps = int(instruction[1:])
        
        if turn == 'R':

            direction = (direction + 1) % 4

        else:

            direction = (direction - 1) % 4
        
        if direction == 0:

            y += steps

        elif direction == 1:

            x += steps

        elif direction == 2:

            y -= steps

        elif direction == 3:

            x -= steps
    
    distance = abs(x) + abs(y)

    return distance

# Calculate and print the distance
distance = calculate_distance(commands)

print("The shortest distance to the destination is:", distance)


## PART 2 ----------------------------------------------------------------------------------------------------------

### updated function
def calculate_distance(instructions):

    x, y = 0, 0  # Starting point
    direction = 0  # 0: North, 1: East, 2: South, 3: West

    visited_locations = set()
    
    for instruction in instructions:

        turn = instruction[0]
        steps = int(instruction[1:])
        
        if turn == 'R':

            direction = (direction + 1) % 4
        else:

            direction = (direction - 1) % 4
        
        for _ in range(steps):

            if direction == 0:
                y += 1

            elif direction == 1:

                x += 1

            elif direction == 2:

                y -= 1

            elif direction == 3:

                x -= 1
            
            if (x, y) in visited_locations:

                distance = abs(x) + abs(y)

                return distance
            
            else:

                visited_locations.add((x, y))
    
    return None  # No location visited twice

# Calculate and print the distance to the first location visited twice
distance = calculate_distance(commands)

if distance is not None:

    print("The distance to the first location visited twice is:", distance)

else:

    print("No location was visited twice.")


