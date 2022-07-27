with open("input") as f:
    integers = f.read().split(",")

integers = [int(string) for string in integers]
integers_part_2 = integers.copy()


def part1(integer_list):
    run = True

    while run:

        for i in range(0, len(integer_list) - 4, 4):
            opcode = integer_list[i:i + 4]

            if opcode[0] == 99:
                run = False

            elif opcode[0] == 1:
                first_value = integer_list[opcode[1]]
                second_value = integer_list[opcode[2]]
                integer_list[opcode[3]] = first_value + second_value

            elif opcode[0] == 2:
                first_value = integer_list[opcode[1]]
                second_value = integer_list[opcode[2]]
                integer_list[opcode[3]] = first_value * second_value

    return integer_list[0]


print("Solution Part 1:", part1(integers))


# Part 2


def part2(integer_list_2):

    copy = integer_list_2.copy()
    searched_output = 19690720

    for noun in range(0, 100, 1):
        for verb in range(0, 100, 1):
            integer_list_2 = copy.copy()
            integer_list_2[1] = noun
            integer_list_2[2] = verb

            curr_solution = part1(integer_list_2)

            if curr_solution == searched_output:
                return 100 * noun + verb


print("Solution Part 2:", part2(integers_part_2))

