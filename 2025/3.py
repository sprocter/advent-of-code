test_inp = """
"""

my_inp = """
"""

def part1(inp):
    total = 0
    for line in inp.splitlines():
        max = -1
        idx = -1
        max_idx = -1
        for digit in list(line)[:-1]:
            idx += 1
            if int(digit) > max:
                max = int(digit)
                max_idx = idx
        first_digit = str(max)
        max = -1
        idx = -1
        for digit in list(line)[max_idx+1:]:
            if int(digit) > max:
                max = int(digit)
        joltage = int(first_digit + str(max))
        total += joltage
    return total

def part2(inp):
    total = 0
    for line in inp.splitlines():
        digits = []
        start = 0
        end = -12
        for _ in range(12):
            end += 1
            for digit in range(9, 0, -1):
                s = str(digit)
                if end == 0:
                    end = None
                if s in line[start:end]:
                    start = line.index(s, start, end)+1
                    digits.append(s)
                    break
        joltage = int(''.join(digits))
        # print(f"Joltage: {joltage}")
        total += joltage
    return total

inp = my_inp
print(f"Part 1: {part1(inp)}")
print(f"Part 2: {part2(inp)}")

# P1, guess 1: 17074. Correct.
# P2, guess 1: 169512729575727. Correct.