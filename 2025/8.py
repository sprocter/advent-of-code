from scipy.spatial import KDTree
from scipy.optimize import bisect

my_inp = """
"""

test_input = """
"""


def _parse_input(inp: str) -> list[list[int]]:
    y = []
    for line in inp.splitlines():
        y.append([int(num) for num in line.split(",")])
    return y


def _get_max_dist_p1(x: int, tgt: int) -> int:
    # We should find the first tgt pairs
    return len(kdt.query_pairs(round(x))) - tgt


def _get_max_dist_p2(x: int, tgt: int) -> int:
    circuits = _merge_junction_boxes(kdt.query_pairs(round(x)))
    if len(circuits) == 0:
        return -1000
    else:
        return (
            # Everything should merge into one circuit
            (len(circuits) - 1)
            +
            # And every junction box should be included
            (len(circuits[0]) - tgt + 1)
        )


def _merge_junction_boxes(pairs: list[tuple[int, int]]) -> list[set[int]]:
    circuits = []
    for jBox1, jBox2 in pairs:
        added = False
        circuits_to_merge = []
        for circuit in circuits:
            if (jBox1 in circuit) or (jBox2 in circuit):
                added = True
                circuits_to_merge.append(circuit)
        if added:
            new_circuit = set([jBox1, jBox2])
            for circuit in circuits_to_merge:
                circuits.remove(circuit)
                new_circuit |= circuit
            circuits.append(new_circuit)
        else:
            circuits.append(set([jBox1, jBox2]))
    return circuits


def _mult_three_largest_circuits(circuits: list[set[int]]) -> int:
    circuit_lengths = []
    for circuit in circuits:
        circuit_lengths.append(len(circuit))
    list.sort(circuit_lengths, reverse=True)
    return circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]


def part1(num_pairs: int) -> int:
    max_dist = round(bisect(_get_max_dist_p1, 0, 15000, (num_pairs)))
    pairs = kdt.query_pairs(max_dist)
    circuits = _merge_junction_boxes(pairs)
    answer = _mult_three_largest_circuits(circuits)
    return answer


def _collect_vertices(pairs) -> set[int]:
    vertices = set()
    for v1, v2 in pairs:
        vertices.add(v1)
        vertices.add(v2)
    return vertices


def part2() -> int:
    max_dist = round(bisect(_get_max_dist_p2, 0, 15000, (len(y))))
    # I'm probably using it wrong but bisect only gets close
    while _get_max_dist_p2(max_dist, len(y)) == 0:
        max_dist += 1
    all_vertices = _collect_vertices(kdt.query_pairs(max_dist))
    all_but_one_vertices = _collect_vertices(kdt.query_pairs(max_dist - 1))
    last_vtx_id = (all_vertices - all_but_one_vertices).pop()
    last_vtx_coords = y[last_vtx_id]
    v1, v2 = kdt.query(last_vtx_coords, 2)[1]
    if int(v1) == last_vtx_id:
        nearest_neighbor_id = int(v2)
    else:
        nearest_neighbor_id = int(v1)
    nearest_neighbor_coords = y[nearest_neighbor_id]
    answer = last_vtx_coords[0] * nearest_neighbor_coords[0]
    return answer


test = False

if test:
    inp = test_input
else:
    inp = my_inp

y = _parse_input(inp)
kdt = KDTree(y)

if test:
    print(part1(10))
else:
    print(part1(1000))

print(part2())

# P1, guess 1: 3696. Too low.
# P1, guess 2: 57564. Correct.
# P2, guess 1: 6725788601. Too high.
# P2, guess 2: 6429279143. Too high.
# P2, guess 3: 133296744. Correct.
