with open("input.txt") as f:
    present = f.read().splitlines()

present = []
print(present)

sum_wrapping_paper = 0

for dimension in present:
    measurements = dimension.split("x")
    length = int(measurements[0])
    width = int(measurements[1])
    height = int(measurements[2])

    wrapping_paper = 2 * length * width + 2 * width * height + 2 * height * length

    lw = length * width
    wh = width * height
    hl = height * length

    if lw <= wh and lw <= hl:
        slack = lw
    elif wh <= lw and wh <= hl:
        slack = wh
    elif hl <= lw and hl <= wh:
        slack = hl

    sum_wrapping_paper += wrapping_paper + slack

print(sum_wrapping_paper)


#Part 2

sum_ribbon = 0

for dimension in present:
    measurements = dimension.split("x")
    length = int(measurements[0])
    width = int(measurements[1])
    height = int(measurements[2])

    measures = []
    measures.extend([length, width, height])
    measures.sort()

    present_ribbon = measures[0] * 2 + measures[1] * 2
    bow_ribbon = length * width * height

    sum_ribbon += present_ribbon + bow_ribbon

print(sum_ribbon)