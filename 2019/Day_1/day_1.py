with open("input") as f:
    fuel_requirements = f.read().splitlines()

solution = [int(x) // 3 - 2 for x in fuel_requirements]

print("Solution Part 1:", sum(solution))

# Part 2
solution_2 = []

for fuel in fuel_requirements:
    negative_fuel = False
    temp = int(fuel)
    while not negative_fuel:
        temp = temp // 3 - 2
        if temp < 0:
            negative_fuel = True
        else:
            solution_2.append(temp)


print("Solution Part 2:", sum(solution_2))

