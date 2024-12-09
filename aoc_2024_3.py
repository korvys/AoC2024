from aocd import get_puzzle
import re

YEAR = 2024
DAY = 3

def parse_data(input_data):
    print(input_data)
    #instructions = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    instructions = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")

    print (instructions.findall(input_data))

def solve_part_a(input_data):
    total = 0
    for inst in filter(lambda x: x[0] == 'mul', parse_data(input_data)):
        total += (int(inst[1]) * int(inst[2]))
    return total

def solve_part_b(input_data):
    total = 0
    do = True
    for inst in parse_data(input_data):
        if do:
            if inst[0] == 'mul':
                total += (int(inst[1]) * int(inst[2]))
            elif inst[4] == ("don't"):
                do = False
        else:
            if inst[3] == 'do':
                do = True

    return total

if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    # print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_a}')
    #print(f'Proposed example answer: {solve_part_a(puzzle.examples[0].input_data)}')
    #print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    # print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')