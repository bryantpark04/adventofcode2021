def part1(f):
    prev = 9999999
    times = 0
    for line in f:
        curr = int(line)
        times += curr > prev
        prev = curr
    print(times) # 1139


def part2(f):
    lines = list(map(int, f.readlines()))
    times = 0
    prev = 999999999999
    for i in range(len(lines)-2):
        curr = sum(lines[i:i+3])
        times += (curr > prev)
        prev = curr
    print(times) # 1103


with open("day1input.txt", "r") as f:
    part2(f)
