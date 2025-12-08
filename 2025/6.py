my_inp = """
"""

test_inp = """  
"""

def part1(inp : str) -> int:
    hw = []
    i = -1
    total = 0
    for line in inp.splitlines():
        i += 1
        hw.append([])
        j = -1
        for item in line.split():
            j += 1
            if item.isnumeric():
                hw[i].append(int(item))
            else:
                if item == "*":
                    total += mult(hw, j)
                else:
                    total += add(hw, j)
    return total

def mult(hw : list[list[int]], col : int) -> int:
    prod = 1
    for row in hw[:-1]:
        prod *= row[col]
    return prod

def add(hw : list[list[int]], col : int) -> int:
    total = 0
    for row in hw[:-1]:
        total += row[col]
    return total

def part2(inp : str) -> int:
    grid = []
    num_rows = len(inp.splitlines())
    operands = []
    num = ''
    total = 0

    for line in inp.splitlines():
        grid.append(list(line))
    for col in range(len(grid[0])):
        for i in range(num_rows):
            num += grid[i][col]
        if not num[-1].isspace():
            op = num[-1]
        num = num[:-1].strip()
        if num.isnumeric():
            operands.append(int(num))
            num = ''
        else:
            if op == "*":
                subtotal = 1
                for operand in operands:
                    subtotal *= operand
            else: # op = "+"
                subtotal = 0
                for operand in operands:
                    subtotal += operand
            operands = []
            total += subtotal
    return total

inp = my_inp
print(part1(inp))
print(part2(inp))

# P1, guess 1: 5733696195703. Correct.
# P2, guess 1: 10951882745757. Correct.