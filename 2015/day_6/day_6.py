import numpy as np

with open("input.txt") as file:
    data = file.read().splitlines()


grid = np.full((1000, 1000), 0)

for sentence in data:

    words = sentence.split()

    if len(words) == 4:
        x1, y1 = map(int, words[1].split(","))
        x2, y2 = map(int, words[3].split(","))

    else:
        x1, y1 = map(int, words[2].split(","))
        x2, y2 = map(int, words[4].split(","))

    if sentence.startswith("turn on"):
        
        grid[x1:x2 + 1, y1:y2 + 1] = 1

    elif sentence.startswith("turn off"):

        grid[x1:x2 + 1, y1:y2 + 1] = 0

    elif sentence.startswith("toggle"):

        grid[x1:x2 + 1, y1:y2 + 1] = 1 - grid[x1:x2 + 1, y1:y2 + 1]

print("Solution 1:", np.count_nonzero(grid))


# Part 2

grid_2 = np.full((1000, 1000), 0)

for sentence in data:

    words = sentence.split()

    if len(words) == 4:
        x1, y1 = map(int, words[1].split(","))
        x2, y2 = map(int, words[3].split(","))

    else:
        x1, y1 = map(int, words[2].split(","))
        x2, y2 = map(int, words[4].split(","))

    if sentence.startswith("turn on"):
        
        grid_2[x1:x2 + 1, y1:y2 + 1] += 1

    elif sentence.startswith("turn off"):

        for x in range(x1, x2 + 1):

            for y in range(y1, y2 + 1):

                if grid_2[x, y] == 0:

                    grid_2[x, y] = 0

                else:
                    grid_2[x, y] -= 1

    elif sentence.startswith("toggle"):

        grid_2[x1:x2 + 1, y1:y2 + 1] += 2

print("Solution 2:", grid_2.sum())
