from ortools.sat.python import cp_model

my_inp = """
"""

test_inp = """
"""


def _parse_inp(inp):
    machines = []
    for line in inp.splitlines():
        pt1tgt = set()
        pt2tgt = []
        buttons = []
        for block in line.split(" "):
            button = set()
            if block[0] == "[":
                for i in range(1, len(block)):
                    if block[i] == "#":
                        pt1tgt.add(i - 1)
            elif block[0] == "(":
                block_trimmed = block[1:-1]
                for num in block_trimmed.split(","):
                    button.add(int(num))
                buttons.append(button)
            elif block[0] == "{":
                block_trimmed = block[1:-1]
                for num in block_trimmed.split(","):
                    pt2tgt.append(int(num))
        machines.append((pt1tgt, buttons, pt2tgt))
    return machines


def _bfs_pt1(m) -> int:
    Q = []
    seen = []
    seen.append({})
    for x in m[1]:
        Q.extend((x, y, 1) for y in m[1])
    while True:
        (state, button, depth) = Q.pop(0)
        if state not in seen:
            seen.append(state)
        if state == m[0]:
            # print(f"{m[0]} needs {depth} presses")
            return depth
        else:
            new_depth = depth + 1
            new_state = state ^ button
            if new_state not in seen:
                Q.extend((new_state, y, new_depth) for y in m[1])


def _cpsolver_pt2(m) -> int:
    model = cp_model.CpModel()
    counter_to_buttons = {}
    button_to_var = {}
    for i in range(len(m[2])):
        counter_to_buttons[i] = []
    for button in m[1]:
        button_to_var[str(button)] = model.new_int_var(0, 265, str(button))
        for counter in button:
            counter_to_buttons[counter].append(button)
    for i in range(len(m[2])):
        vs = []
        for button in counter_to_buttons[i]:
            button_str = str(button)
            vs.append(button_to_var[button_str])
        model.add(sum(vs) == m[2][i])

    model.minimize(sum(button_to_var.values()))

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    presses = 0
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for v in button_to_var.values():
            presses += solver.value(v)

    return presses


def part1(machines) -> int:
    total_presses = 0
    for machine in machines:
        total_presses += _bfs_pt1(machine)
    return total_presses


def part2(machines) -> int:
    total_presses = 0
    for machine in machines:
        total_presses += _cpsolver_pt2(machine)
    return total_presses


machines = _parse_inp(my_inp)
# print(part1(machines))
print(part2(machines))


# P1, guess 1: 502. Correct.
# P2, guess 1: 21467. Correct.
