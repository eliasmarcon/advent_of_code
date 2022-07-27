with open("input") as f:
    input = f.read().splitlines()


heatmap = [[int(number) for number in string] for string in input]
lowpoints = []

for row in range(0, len(heatmap)):

    for col in range(0, len(heatmap[row])):

        cur_item = heatmap[row][col]

        if row + 1 < len(heatmap) and cur_item >= heatmap[row + 1][col]:
            continue

        if row - 1 >= 0 and cur_item >= heatmap[row - 1][col]:
            continue

        if col + 1 < len(heatmap[row]) and cur_item >= heatmap[row][col + 1]:
            continue

        if col - 1 >= 0 and cur_item >= heatmap[row][col - 1]:
            continue

        lowpoints.append(cur_item)

print("Lowpoints:", lowpoints)

lowpoints = [x + 1 for x in lowpoints]

print("Solution Part 1:", sum(lowpoints))







