with open("input") as f:
    console = f.read().splitlines()


def part_one(console_input):
    operation = []
    argument = []
    boolean = []
    accumulator = 0
    i = 0
    found_double = False

    for item in console_input:
        temp = item.split()
        operation.append(temp[0])
        argument.append(temp[1])
        boolean.append(False)

    while i < len(operation):

        operation_temp = operation[i]
        argument_temp = argument[i]

        if boolean[i]:
            found_double = True
            break

        if operation_temp == "acc":

            accumulator += int(argument_temp)
            boolean[i] = True
            i += 1
            continue

        elif operation_temp == "jmp":

            boolean[i] = True
            i += int(argument_temp)
            continue

        else:
            boolean[i] = True
            i += 1
            continue

    return accumulator, found_double


print("Solution Part 1:", part_one(console)[0])


# Part 2

def part_two(console_input):
    run = True
    index = 0

    while run and index < len(console_input):
        found = False

        while not found and index < len(console_input):
            string = console_input[index]
            operation = string.split(" ")
            if operation[0] == "nop":
                found = True
                old = "nop"
                new = "jmp"
                console_input[index] = new + " " + operation[1]

            elif operation[0] == "jmp":
                found = True
                old = "jmp"
                new = "nop"
                console_input[index] = new + " " + operation[1]

            else:
                index += 1

        solution = part_one(console_input)

        if solution[1]:
            console_input[index] = old + " " + operation[1]

        else:
            run = False

        index += 1

    return solution


print("Solution Part 2:", part_two(console)[0])
