with open("input") as file:

    password_strings = [line.strip() for line in file.readlines()]

## PART 1 ----------------------------------------------------------------------------------------------------------
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

keypad_position = (1, 1)

# List to store the bathroom code
bathroom_code = []

# Function to move on the keypad based on instructions
def move_button(direction, button):

    x, y = button

    if direction == "U" and x > 0:

        return (x - 1, y)
    
    elif direction == "D" and x < 2:
    
        return (x + 1, y)
    
    elif direction == "L" and y > 0:
    
        return (x, y - 1)
    
    elif direction == "R" and y < 2:
    
        return (x, y + 1)
    
    return button

# Process each set of instructions
for instruction in password_strings:

    for step in instruction:

        keypad_position = move_button(step, keypad_position)

    bathroom_code.append(str(keypad[keypad_position[0]][keypad_position[1]]))

# Combine the digits to form the bathroom code
bathroom_code_str = ''.join(bathroom_code)

print("The bathroom code is:", bathroom_code_str)


## PART 2 ----------------------------------------------------------------------------------------------------------

# Define the updated keypad layout
keypad = [
    [' ', ' ', '1', ' ', ' '],
    [' ', '2', '3', '4', ' '],
    ['5', '6', '7', '8', '9'],
    [' ', 'A', 'B', 'C', ' '],
    [' ', ' ', 'D', ' ', ' ']
]

# Starting button
keypad_position = (2, 0)

# List to store the bathroom code
bathroom_code = []

# Function to move on the keypad based on instructions
def move_button(direction, button):

    x, y = button
    
    if direction == "U" and x > 0 and keypad[x - 1][y] != ' ':
    
        return (x - 1, y)
    
    elif direction == "D" and x < 4 and keypad[x + 1][y] != ' ':
    
        return (x + 1, y)
    
    elif direction == "L" and y > 0 and keypad[x][y - 1] != ' ':
    
        return (x, y - 1)
    
    elif direction == "R" and y < 4 and keypad[x][y + 1] != ' ':
    
        return (x, y + 1)
    
    return button

# Process each set of instructions
for instruction in password_strings:

    for step in instruction:
    
        keypad_position = move_button(step, keypad_position)
    
    bathroom_code.append(str(keypad[keypad_position[0]][keypad_position[1]]))

# Combine the digits to form the bathroom code
bathroom_code_str = ''.join(bathroom_code)

print("The bathroom code is:", bathroom_code_str)