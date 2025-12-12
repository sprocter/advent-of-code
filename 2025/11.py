from copy import deepcopy

my_inp = """
"""

test_inp = """
"""

test_inp2 = """
"""

def _parse_inp(inp):
    graph = {}
    for line in inp.splitlines():
        tokens = line.split()
        graph[tokens[0][:-1]] = tokens[1:]
    return graph


def _bfs_pt1(g, start, end) -> int:
    paths = 0

    Q = []
    seen = set()
    seen.add(start)
    Q.append(start)
    while len(Q) > 0:
        cur = Q.pop(0)
        seen.add(cur)
        if cur not in g:
            continue
        for v in g[cur]:
            if v == end:
                paths += 1
            elif v not in seen:
                Q.append(v)
    return paths


def part1(graph) -> int:
    return _bfs_pt1(graph, "you", "out")


def _dfs_pt2(g, v, seen, end, pathCount):
    seen.add(v)
    if v == end:
        if pathCount > 0 and pathCount % 10000 == 0:
            print(f"Total valid paths (so far): {pathCount}")
        return pathCount + 1
    else:
        for w in g[v]:
            if w not in seen:
                pathCount = _dfs_pt2(g, w, deepcopy(seen), end, pathCount)
    return pathCount


def _reverse_graph(g):
    rgraph = {}
    for key in g.keys():
        for value in g[key]:
            if value not in rgraph:
                rgraph[value] = []
            rgraph[value].append(key)
    return rgraph

def _get_ancestors(rg, node):
    ancestors = set()
    Q = []
    Q.append(node)
    while len(Q) > 0:
        cur = Q.pop(0)
        ancestors.add(cur)
        for n in rg[cur]:
            if n not in ancestors and n not in Q:
                Q.append(n)
    return ancestors

def part2(graph) -> int:
    rgraph = _reverse_graph(graph)
    rgraph["svr"] = []

    fft_ancestors = _get_ancestors(rgraph, "fft")
    dac_ancestors = _get_ancestors(rgraph, "dac")

    graph["out"] = []
    svr_to_fft = _dfs_pt2(graph, "svr", graph.keys() - fft_ancestors, "fft", 0)
    print(f"svr_to_fft = {svr_to_fft}")

    fft_to_dac = _dfs_pt2(graph, "fft", graph.keys() - dac_ancestors, "dac", 0)
    print(f"fft_to_dac = {fft_to_dac}")

    dac_to_out = _dfs_pt2(graph, "dac", set(), "out", 0)
    print(f"dac_to_out = {dac_to_out}")

    valid_paths = svr_to_fft * fft_to_dac * dac_to_out
    return valid_paths

graph = _parse_inp(my_inp)
print(part1(graph))
print(part2(graph))

# P1, guess 1: 719. Correct.
# P2, guess 1: 337433554149492. Correct.