with open("input") as f:
    tree_map = f.read().splitlines()

print(tree_map)


def count_trees(flight_map, step_right=3, step_down=1, tree ="#"):
    index = 0
    tree_counter = 0

    for row in flight_map[step_down::step_down]:
        index += step_right
        row_item = index % len(row)
        if row[row_item] == tree:
            tree_counter += 1

    return tree_counter


trees_3_1 = count_trees(tree_map)
print("Solution Part 1:", trees_3_1)

# Part 2
trees_collection = []

trees_1_1 = count_trees(tree_map, 1, 1)
trees_5_1 = count_trees(tree_map, 5, 1)
trees_7_1 = count_trees(tree_map, 7, 1)
trees_1_2 = count_trees(tree_map, 1, 2)

trees_collection.extend([trees_3_1, trees_1_1, trees_5_1, trees_7_1, trees_1_2])

multiplied = 1

for tree in trees_collection:
    multiplied *= tree

print("Solution Part 2:", multiplied)
