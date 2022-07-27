from functools import reduce

with open("input") as f:
    timestamp_bus = f.read().splitlines()

timestamp = int(timestamp_bus[0])
string_buses = timestamp_bus[1]
buses_original = []
buses = []
string_buses = string_buses.split(",")

for bus in string_buses:
    if bus != "x":
        temp = int(bus)
        buses.append(0)
        buses_original.append(temp)

# Part 1

departed = False
time = 1
min_distance = 0
minute = 0
bus_id = 0

while not departed:

    for i in range(0, len(buses)):

        if time % buses_original[i] == 0:
            buses[i] += buses_original[i]

        if buses[i] == timestamp:
            minute = buses[i] - timestamp
            index = buses.index(buses[i])
            bus_id = buses_original[index]
            departed = True

    if time > timestamp:

        for i in range(0, len(buses)):

            if buses[i] - timestamp > 0:
                minute = buses[i] - timestamp
                index = buses.index(buses[i])
                bus_id = buses_original[index]
                departed = True

    print("Timestamp", time, ":", buses)
    time += 1

print("Solution Part 1:", bus_id * minute)

# Part 2
with open("input", "r") as fp:
    lines = fp.readlines()
timestamp = int(lines[0][:-1])
bus_ids = [int(x) for x in lines[1].split(",") if x.isdigit()]

LINES = lines
start = int(LINES[0])
busses = ["x" if x == "x" else int(x) for x in LINES[1].split(",")]


def part2():
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val


print("Solution Part 2:", part2())
