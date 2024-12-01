from aocd import get_puzzle

YEAR = 2024
DAY = 1

def parse_input(input_data):
    pairs = input_data.splitlines()
    left_list, right_list = map(list, zip(*[map(int, pair.split()) for pair in pairs]))

    return left_list, right_list


def solve_part_a(input_data):
    left_list, right_list = parse_input(input_data)

    recombined_sorted_list = list(zip(sorted(left_list), sorted(right_list)))
    total_distance = sum([abs(l[0]-l[1]) for l in recombined_sorted_list])
    return total_distance


def solve_part_b(input_data):
    left_list, right_list = parse_input(input_data)
    location_count = {}

    for location in right_list:
        location_count[location] = location_count.get(location, 0) + 1
    similarity = sum([location_count.get(location, 0)*location for location in left_list])
    return similarity


if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    print(f'Answered: {puzzle.answered_a}')
    print(f'Example answer: {puzzle.examples[0].answer_a}')
    print(f'Proposed example answer: {solve_part_a(puzzle.examples[0].input_data)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    print()
    print('Part 2')
    print(f'Answered: {puzzle.answered_b}')
    print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b(puzzle.examples[0].input_data)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')

