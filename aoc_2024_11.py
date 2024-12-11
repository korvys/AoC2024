from time import perf_counter

from aocd import get_puzzle
from collections import Counter

import math

YEAR = 2024
DAY = 11

example_data_a = '125 17'
example_data_b = example_data_a

f = Counter()
g = Counter()

def parse_data(input_data):
    stones = [int(stone) for stone in input_data.split()]
    for stone in stones:
        f[stone] += 1
    return set(stones)

def change(stone):
    f_stone = f[stone]
    if stone == 0:
        g[1] += f_stone
        return [1]

    digits = int(math.log10(stone))+1
    if digits % 2 == 0:
        first_half = math.floor(stone//10**(digits//2))
        second_half = stone - first_half*10**(digits//2)
        g[first_half] += f_stone
        g[second_half] += f_stone
        return [first_half, second_half]

    big_stone = stone*2024
    g[big_stone] += f_stone
    return [big_stone]

def blink(stones):
    new_stones = set()
    global f, g
    g = Counter()
    for stone in stones:
        new_stones.update(change(stone))
    f = g
    return new_stones

def solve_part_a(input_data):
    global f, g
    f = Counter()
    g = Counter()
    stones = parse_data(input_data)

    for i in range(25):
        start = perf_counter()
        stones = blink(stones)
        stop = perf_counter()
        #print(f"After blink {i+1} ({stop-start:.2f}s):\n{f.total()}")

    return f.total()


def solve_part_b(input_data):
    global f, g
    f = Counter()
    g = Counter()
    stones = parse_data(input_data)

    for i in range(75):
        start = perf_counter()
        stones = blink(stones)
        stop = perf_counter()
        #print(f"After blink {i + 1} ({stop - start:.2f}s):\n{f.total()}")

    return f.total()

if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example data: {example_data_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_a}')
    print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_b}')
    # print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')