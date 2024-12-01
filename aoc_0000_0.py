from aocd import get_puzzle

YEAR = 0000
DAY = 0

def solve_part_a(input_data):
    pass

def solve_part_b(input_data):
    pass

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