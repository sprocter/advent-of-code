import shapely

my_inp = """
"""

test_inp = """
"""

def part1(inp : str) -> int:
    pts = []
    max_area = -1
    for line in inp.splitlines():
        x, y = line.split(",")
        pts.append((int(x),int(y)))
    for pt1 in pts:
        x1 = pt1[0]
        y1 = pt1[1]
        for pt2 in pts:
            x2 = pt2[0]
            y2 = pt2[1]
            area = (abs(x1-x2)+1)*(abs(y1-y2)+1)
            if area > max_area:
                max_area = area
    return max_area


def part2(inp : str) -> int:
    pts = []
    max_area = -1
    for line in inp.splitlines():
        x, y = line.split(",")
        pts.append((int(x),int(y)))
    
    p = shapely.Polygon(pts)

    for pt1 in pts:
        x1 = pt1[0]
        y1 = pt1[1]
        for pt2 in pts:
            x2 = pt2[0]
            y2 = pt2[1]
            s = shapely.Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
            if p.covers(s):
                area = (abs(x1-x2)+1)*(abs(y1-y2)+1)
                if area > max_area:
                    max_area = area
    
    return max_area


inp = my_inp
print(part1(inp))
print(part2(inp))


# P1, guess 1: 4764078684. Correct.
# P2, guess 1: 1652344888. Correct.