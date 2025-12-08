my_inp = """
"""

test_inp = """
"""

def part1(inp : str) -> int:
    grid = []
    splitcount = 0
    for line in inp.splitlines():
        grid.append(list(line))
    s_idx = grid[0].index("S")
    grid[1][s_idx] = "|"
    for row in range(2, len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                if grid[row-1][col] == "|":
                    grid[row][col] = "|"
            elif grid[row][col] == "^":
                if grid[row-1][col] == "|":
                    splitcount += 1
                    if col > 0:
                        grid[row][col-1] = "|"
                    if col < len(grid):
                        grid[row][col+1] = "|"
    return splitcount

def part2(inp : str) -> int:
    grid = []
    active_cols = []
    for line in inp.splitlines():
        grid.append(list(line))
    s_idx = grid[0].index("S")
    grid[1][s_idx] = "|"
    for row in range(2, len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                if grid[row-1][col] == "|":
                    grid[row][col] = "|"
            elif grid[row][col] == "^":
                if grid[row-1][col] == "|":
                    grid[row][col-1] = "|"
                    grid[row][col+1] = "|"
    grid[1][s_idx] = 1
    paths = walkgridCalc(grid)
    return paths

def prepGrid(grid):
    new_grid = []
    for line in grid:
        new_line = [0 if x=="." else x for x in line] # to sum w/ empty cells
        new_line = [0] + new_line + [0] # avoid bounds checking
        new_grid.append(new_line)
    return new_grid

def walkgridCalc(grid):
    grid = prepGrid(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])-1):
            aLeft = grid[row-1][col-1]
            above = grid[row-1][col]
            aRight = grid[row-1][col+1]
            left = grid[row][col-1]
            right = grid[row][col+1]
            if grid[row][col] == "|":
                cell = above
                if right == "^":
                    cell += aRight
                if left == "^":
                    cell += aLeft
                grid[row][col] = cell
    return sum(grid[row])


inp = my_inp
print(part1(inp))
print(part2(inp))

# P1, guess 1: 1504. Correct.
# P2, guess 1: 5137133207830. Correct.