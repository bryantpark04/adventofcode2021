def part1(lines):
    x, y = 0, 0
    for l in lines:
        direction, magnitude = l.split()
        magnitude = int(magnitude)
        if direction == "forward":
            x += magnitude
        elif direction == "down":
            y += magnitude
        elif direction == "up":
            y -= magnitude
    print(x * y) # 2091984


def part2(lines):
    x, y = 0, 0
    aim = 0
    for l in lines:
        direction, magnitude = l.split()
        magnitude = int(magnitude)
        if direction == "forward":
            x += magnitude
            y += magnitude * aim
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude
    print(x * y) # 2086261056


with open("day2input.txt", "r") as f:
    lines = f.readlines()
    part2(lines)