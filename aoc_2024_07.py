from aocd import get_puzzle
from pprint import pprint
from itertools import product

YEAR = 2024
DAY = 7

example_data_a = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
example_data_b = example_data_a

class Equation():
    def __init__(self, raw):
        split_eq = raw.split(': ')
        self.answer = int(split_eq[0])
        self.inputs = [int(value) for value in split_eq[1].split()]

    def __repr__(self):
        return f"{self.answer}: {' '.join(map(str, self.inputs))}"

    def __str__(self):
        return self.__repr__()

def parse_data(input_data):
    equations = [Equation(line) for line in input_data.splitlines()]
    return equations

def mul(a, b):
    return a*b

def add(a, b):
    return a+b

def concat(a, b):
    return int(str(a)+str(b))

def solve_part_a(input_data):
    operators = [mul, add]
    equations = parse_data(input_data)
    total_calibration_result = 0
    for equation in equations:
        for operator_sequence in product(operators, repeat=len(equation.inputs)-1):
            current_value = equation.inputs[0]
            for i, operator in enumerate(operator_sequence, start=1):
                current_value = operator(current_value, equation.inputs[i])
            if equation.answer == current_value:
                print(f"'{equation}' can be solved with {operator_sequence}")
                total_calibration_result += equation.answer
                break
        else:
            print(f"'{equation}' cannot be solved")

    return total_calibration_result

def solve_part_b(input_data):
    operators = [mul, add, concat]
    equations = parse_data(input_data)
    total_calibration_result = 0
    for equation in equations:
        for operator_sequence in product(operators, repeat=len(equation.inputs) - 1):
            current_value = equation.inputs[0]
            for i, operator in enumerate(operator_sequence, start=1):
                current_value = operator(current_value, equation.inputs[i])
            if equation.answer == current_value:
                print(f"'{equation}' can be solved with {operator_sequence}")
                total_calibration_result += equation.answer
                break
        else:
            print(f"'{equation}' cannot be solved")

    return total_calibration_result

if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_a}')
    # print(f'Example data: {example_data_a}')
    # print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    # print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')