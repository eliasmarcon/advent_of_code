with open("input") as f:
    depths = f.read().splitlines()

depths_int = []

for depth in depths:
    temp = int(depth)
    depths_int.append(temp)

counter = 0

# Part 1
for i in range(1, len(depths_int)):
    if depths_int[i] > depths_int[i - 1]:
        counter += 1

print("Solution Part 1:", counter)

# Part 2
sums = []
counter_sums = 0

for i in range(0, len(depths_int) - 2):
    temp = depths_int[i] + depths_int[i + 1] + depths_int[i + 2]
    sums.append(temp)

for i in range(0, len(sums) - 1):
    if sums[i + 1] > sums[i]:
        counter_sums += 1

print("Solution Part 2:", counter_sums)
