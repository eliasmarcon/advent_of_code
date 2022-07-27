with open("input") as f:
    expenses = f.read().splitlines()

print(expenses)

product = 0

for expense in expenses:
    for expense2 in expenses:
        if int(expense) + int(expense2) == 2020:
            product = int(expense) * int(expense2)

print("Solution Part 1:", product)

# Part 2
product2 = 0

for expense in expenses:
    for expense2 in expenses:
        for expense3 in expenses:
            if int(expense) + int(expense2) + int(expense3) == 2020:
                product2 = int(expense) * int(expense2) * int(expense3)

print("Solution Part 2:", product2)
