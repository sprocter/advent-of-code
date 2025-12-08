import math

test_inp = """"""

my_inp = """"""


def part1(input):
    ranges = input.split(",")
    total = 0
    for r in ranges:
        low, high = r.split("-")
        for i in range(int(low), int(high) + 1):
            s = str(i)
            l = len(s) / 2
            if l != round(l):
                continue
            l = int(l)
            if s[:l] == s[l:]:
                total += i
    return total

def part2(input):
    ranges = input.split(",")
    total = 0
    for r in ranges:
        low, high = r.split("-")
        for idnum in range(int(low), int(high) + 1):
            s = str(idnum)
            half = math.floor(len(s) / 2)
            for subid_len in range(1, half+1):
                if len(s) % subid_len != 0:
                    continue
                repeated_seq = s[:subid_len] * int(len(s) / subid_len)
                if repeated_seq == s:
                    total += idnum
                    break
    return total

inp = my_inp
print(part1(inp))
print(part2(inp))
# P1, guess 1: 53420042388. Correct.
# P2, guess 1: 69553832684. Correct.