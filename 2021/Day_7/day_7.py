with open("input") as f:
    crabs = f.read().split(",")

crabs = [int(numeric_string) for numeric_string in crabs]

min_crabs = min(crabs)
max_crabs = max(crabs)

crabs_range = list(range(min_crabs, max_crabs))

# fuel_cost = []
#
# for crab_element in crabs_range:
#
#     counter = 0
#
#     for crab in crabs:
#
#         while crab != crab_element:
#             if crab > crab_element:
#                 crab -= 1
#                 counter += 1
#             else:
#                 crab += 1
#                 counter += 1
#
#     fuel_cost.append(counter)
#
# fuel_cost.sort()
# print(fuel_cost)  # take the first number

# Part 2

fuel_cost = []

for crab_element in crabs_range:

    counter = 0

    for crab in crabs:
        steps = 1

        while crab != crab_element:

            if crab > crab_element:
                crab -= 1
                counter += steps
                steps += 1
            else:
                crab += 1
                counter += steps
                steps += 1

    fuel_cost.append(counter)

fuel_cost.sort()
print("Solution Part 2:", fuel_cost)
