import itertools

my_inp = """
"""

test_inp = """3
"""

test_inp2 = """
"""

test_inp3 = """1
"""
mini = 99999999999999
maxi = -1


def part1(inp: str) -> int:
    global mini, maxi
    ranges = True
    fresh = {}  # low -> high
    numFresh = 0
    spoiled = 0
    for line in inp.splitlines():
        oNF = numFresh
        off = 99999999999999
        off_ref = 0
        if line == "":
            ranges = False
            fresh = dict(sorted(fresh.items()))
            continue
        if ranges:
            low, high = line.split("-")
            if int(low) < mini:
                mini = int(low)
            if int(high) > maxi:
                maxi = int(high)
            if int(low) not in fresh:
                fresh[int(low)] = int(high)
            elif int(high) > fresh[int(low)]:
                fresh[int(low)] = int(high)
        else:
            ingred = int(line)
            for low, high in fresh.items():
                if (ingred >= low) and (ingred <= high):
                    # print(f"Found {ingred} in range {low}-{high}")
                    numFresh += 1
                    break
                else:
                    off_low = abs(low - ingred)
                    off_high = abs(ingred - high)
                    if off > min(off_low, off_high):
                        off = min(off_low, off_high)
                        off_ref = str(low) + "-" + str(high)
            if oNF == numFresh:
                spoiled += 1
                # print(f"{ingred} is spoiled, it was off of {off_ref} by {off}")
    # print(f"{spoiled} ingredients are spoiled")
    return numFresh, fresh


def part2Old(fresh: dict) -> int:
    lfresh = list(fresh)
    nfresh = {}
    fresh_ids = 0
    i = 0
    while i in range(len(lfresh)):
        j = i + 1
        if j < len(lfresh) and (fresh[lfresh[i]] + 1) >= lfresh[j]:
            while j < len(lfresh) - 1 and fresh[lfresh[i]] + 1 >= lfresh[j]:
                j += 1
            nfresh[lfresh[i]] = fresh[lfresh[j]]
            print(f"Merging from {lfresh[i]} to... {fresh[lfresh[j]]}")
            i = j + 1
        else:
            nfresh[lfresh[i]] = fresh[lfresh[i]]
            i += 1
    for low, high in nfresh.items():
        # print(f"Adding ids from {high + 1} to {low}")
        fresh_ids += high + 1 - low
    # print(f"Total ids: {maxi-mini}")
    # print(f"Fresh ids: {fresh_ids}")
    return fresh_ids


def overlaps(a: range, b: range) -> bool:
    # https://scicomp.stackexchange.com/a/26260
    if b.start <= a.stop:
        return True
    else:
        return False


def merge(a: range, b: range) -> range:
    return range(min(a.start, b.start), max(a.stop, b.stop))


def parseRanges(inp: str) -> list[range]:
    ranges = []
    for line in inp.splitlines():
        if line == "":
            return sorted(ranges, key=lambda r: r.start)
        low, high = line.split("-")
        ranges.append(range(int(low), int(high)+1))


def combineRanges(ranges: list[range]) -> list[range]:
    for r1, r2 in itertools.pairwise(ranges):
        if overlaps(r1, r2):
            ranges.remove(r1)
            ranges.remove(r2)
            ranges.append(merge(r1, r2))
            return combineRanges(sorted(ranges, key=lambda r: r.start))
    return ranges


def countRanges(ranges: list[range]) -> int:
    total = 0#len(ranges)
    for r in ranges:
        total += len(r)
    return total


def part2(inp: str) -> int:
    ranges = parseRanges(inp)
    ranges = combineRanges(ranges)
    count = countRanges(ranges)
    return count


inp = my_inp
available_fresh, fresh_dict = part1(inp)
print(available_fresh)
print(part2(inp))

# P1, guess 1: 660. Too low.
# P1, guess 2: 681. Correct.
# P2, guess 1: 526623749886517. Too high.
# P2, guess 2: 416452112710610. Too high.
# P2, guess 3: 361548030866477. Too high.
# P2, guess 4: 82877109136517. Incorrect.
# P2, guess 5: 348820208020387. Incorrect.
# P2, guess 6: 348820208020409. Incorrect.
# P2, guess 7: 348820208020387. Still incorrect 😅
# P2, guess 8: 348820208020395. Incorrect.