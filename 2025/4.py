test_inp = """
"""

my_inp = """
"""

def part1(inp):
    grid = []
    # Build grid
    for line in inp.splitlines():
        row = []
        grid.append(row)
        for elem in list(line):
            row.append(elem)
    del row
    movable = 0
    movable_locs = []
    # Count movable rolls
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if(grid[r][c] == "."):
                continue
            neighbors = 0
            if (r > 0):
                if (c > 0) and (grid[r-1][c-1] == "@"):
                    neighbors += 1
                if grid[r-1][c] == "@":
                    neighbors += 1
                if (c < len(grid[r])-1) and (grid[r-1][c+1] == "@"):
                    neighbors += 1
            if (c > 0) and (grid[r][c-1] == "@"):
                neighbors += 1
            if (c < len(grid[r])-1) and (grid[r][c+1] == "@"):
                neighbors += 1
            if (r < len(grid)-1):
                if (c > 0) and (grid[r+1][c-1] == "@"):
                    neighbors += 1
                if grid[r+1][c] == "@":
                    neighbors += 1
                if (c < len(grid[r])-1) and (grid[r+1][c+1] == "@"):
                    neighbors += 1
            if neighbors < 4:
                movable += 1
                movable_locs.append((r,c))
                # print(f"Movable roll found at Row {r}, Column {c}")
    return movable, movable_locs, grid

def part2(inp):
    moved = 0
    while(True):
        movable, movable_locs, grid = part1(inp)
        moved += movable
        if (len(movable_locs) == 0):
            return moved
        for (r, c) in movable_locs:
            grid[r][c] = "."
        rows = []
        for r in range(len(grid)):
            rows.append(''.join(grid[r]))
        inp = "\n".join(rows) 
    

inp = my_inp
print(part1(inp)[0])
print(part2(inp))

# P1, guess 1: 1342. Too low.
# P1, guess 2: 1349. Correct.
# P2, guess 1: 8277. Correct.