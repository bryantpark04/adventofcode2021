def part1(lines):
    length = len(lines[0].strip())
    mcb = [0] * length
    bits = [[0] * 2] * length
    for line in lines:
        for i in range(length):
            bit = line[i]
            mcb[i] += 1 if bit == "1" else -1
    gamma = "".join("1" if mcb[i] > 0 else "0" for i in range(len(mcb)))
    epsilon = "".join("1" if gamma[i] == "0" else "0" for i in range(length))
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon) # 2743844


def part2(lines):
    length = len(lines[0].strip())
    product = 1
    for target_bit in (0, 1):
        indices = list(range(length))
        for pos in range(length):

            for i in indices: # find the most common bit
                
    return product


with open("day3input.txt", "r") as f:
    lines = f.readlines()
    part1(lines)
