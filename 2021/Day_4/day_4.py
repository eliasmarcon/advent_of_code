with open("input") as f:
    first_line, bingo_table = f.read().split('\n\n', 1)


bingo_table = int(bingo_table)

print(bingo_table)

print(first_line)
