test_inp = """
"""

test_inp2 = """
"""

test_inp3 = """"""

my_inp = """
"""


def part1(dial, inp):
    zeroes = 0
    for line in inp.splitlines():
        if line[0] == "L":
            dial -= int(line[1:])
        elif line[0] == "R":
            dial += int(line[1:])
        if dial % 100 == 0:
            zeroes += 1
    return zeroes

pointing_at = 50

def part2(dial, inp):
    zeroes = 0
    for line in inp.splitlines():
        was_zero = dial == 0
        if line[0] == "L":
            if len(line) > 3:
                zeroes += int(line[1:-2])
                dial -= int(line[-2:])
            else:
                dial -= int(line[1:])
        elif line[0] == "R":
            if len(line) > 3:
                zeroes += int(line[1:-2])
                dial += int(line[-2:])
            else:
                dial += int(line[1:])
        if dial == 0:
            zeroes += 1
        if (was_zero and dial < 0):
            zeroes -= 1
        while dial < 0:
            zeroes += 1
            dial += 100
        while dial >= 100:
            zeroes += 1
            dial -= 100
        # print(f"line = {line}\tdial = {dial}\tzeroes = {zeroes}")
    return zeroes

inp = my_inp
print(part1(pointing_at, inp))
print(part2(pointing_at, inp))

# P1, guess 1: 1129. Correct.
# P2, guess 1: 6649. Too high.
# P2, guess 2: 6543. Too low.
# P2, guess 3: 6638. Correct.