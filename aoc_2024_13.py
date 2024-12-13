from aocd import get_puzzle

YEAR = 2024
DAY = 13

example_data_a = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

example_data_b = example_data_a

def parse_data(input_data):
    blocks = input_data.split('\n\n')
    machines = []
    for block in blocks:
        split_block = block.splitlines()

        ax, ay = tuple([part.split('+')[1] for part in split_block[0].strip().split(': ')[1].split(', ')])
        bx, by = tuple([part.split('+')[1] for part in split_block[1].strip().split(': ')[1].split(', ')])
        cx, cy = tuple([part.split('=')[1] for part in split_block[2].strip().split(': ')[1].split(', ')])
        machines.append(((int(ax), int(ay)), (int(bx), int(by)), (int(cx), int(cy))))
    return machines


def v_shear(location, m):
    x, y = location
    return (x, m*x + y)

def h_shear(location, m):
    x, y = location
    return (x + m*y, y)

def normalise(location, unit_location):
    x1, y1 = location
    x2, y2 = unit_location
    return (x1/x2, y1/y2)

def close_enough(solution):
    return (round(solution[0], 0) == round(solution[0], 2)) and (round(solution[1], 0) == round(solution[1], 2))


def solve_part_a(input_data):
    machines = parse_data(input_data)

    total = 0
    for a, b, c in machines:
        v_shear_m = -a[1]/a[0]
        hx, hy = v_shear((b[0], b[1]), v_shear_m)
        h_shear_m = -hx/hy
        location = c
        unit_location = (a[0]+b[0], a[1]+b[1])

        shear_location = h_shear(v_shear(location, v_shear_m), h_shear_m)
        shear_unit_location = h_shear(v_shear(unit_location, v_shear_m), h_shear_m)

        solution = normalise(shear_location, shear_unit_location)
        if close_enough(solution):
            #print(a, b, c, solution)
            total += int(round(solution[0])) * 3
            total += int(round(solution[1])) * 1

    return total


def solve_part_b(input_data):
    machines = parse_data(input_data)

    total = 0
    for button_a, button_b, prize in machines:
        prize = (prize[0]+10000000000000, prize[1]+10000000000000)
        v_shear_m = -button_a[1] / button_a[0]
        hx, hy = v_shear((button_b[0], button_b[1]), v_shear_m)
        h_shear_m = -hx / hy
        location = prize
        unit_location = (button_a[0] + button_b[0], button_a[1] + button_b[1])

        shear_location = h_shear(v_shear(location, v_shear_m), h_shear_m)
        shear_unit_location = h_shear(v_shear(unit_location, v_shear_m), h_shear_m)

        solution = normalise(shear_location, shear_unit_location)
        if close_enough(solution):
            #print(button_a, button_b, prize, solution)
            total += int(round(solution[0])) * 3
            total += int(round(solution[1])) * 1

    return total


if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example data: {example_data_a}')
    print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')