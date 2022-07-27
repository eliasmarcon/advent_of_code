with open("input") as f:
    joltage_adapters = f.read().splitlines()

joltage_adapters = [int(numeric_string) for numeric_string in joltage_adapters]
built_in_adapter = max(joltage_adapters) + 3
joltage_adapters.append(built_in_adapter)
joltage_adapters.sort()

charging_outlet = 0
counter_joltdiff_one = 0
counter_joltdiff_three = 0

for adapter in joltage_adapters:

    difference = adapter - charging_outlet
    if difference == 1:
        counter_joltdiff_one += 1
    elif difference == 3:
        counter_joltdiff_three += 1

    charging_outlet = adapter

multiplied_joltdiff = counter_joltdiff_one * counter_joltdiff_three

print("Number of 1-jolt differences:", counter_joltdiff_one)
print("Number of 3-jolt differences:", counter_joltdiff_three)
print("Solution Part 1:", multiplied_joltdiff)

# Part 2

# arrangements = []
# charging_outlet_2 = 0
#
# for i in range(0, len(joltage_adapters) - 3):
#
#     three_adapters = joltage_adapters[i:i + 3]
#
#     for adapter in three_adapters:
#         if adapter - charging_outlet_2 <= 3:
#             # row_start = joltage_adapters[:joltage_adapters.index(adapter)]
#             # row_end = joltage_adapters[joltage_adapters.index(adapter):]
#             # print(row_start)
#             # print(row_end)
#             #
#             # index = joltage_adapters.index(adapter)
#             # if index != 0:
#             #     row = row.pop(joltage_adapters[index - 1])
#             row = joltage_adapters[joltage_adapters.index(adapter):]
#             if row not in arrangements:
#                 arrangements.append(row)
#
#     charging_outlet_2 = joltage_adapters[i]
#
# for element in arrangements:
#     print(element)


sol = {0: 1}
for line in joltage_adapters:
    sol[line] = 0
    if line - 1 in sol:
        sol[line] += sol[line - 1]
    if line - 2 in sol:
        sol[line] += sol[line - 2]
    if line - 3 in sol:
        sol[line] += sol[line - 3]

print("Solution Part 2:", sol[max(joltage_adapters)])
