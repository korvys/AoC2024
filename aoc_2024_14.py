from pprint import pprint
from collections import Counter

from aocd import get_puzzle
import re

YEAR = 2024
DAY = 14

example_data_a = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
example_data_b = example_data_a

def vector_add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def vector_multiply(a, b):
    return (a[0]*b, a[1]*b)

def vector_modulo(a, b):
    return (a[0]%b[0], a[1]%b[1])

def parse_data(input_data):
    n = re.compile(r'(-?\d+)')
    robots = []
    for line in input_data.splitlines():
         robot = n.findall(line)
         robots.append([(int(robot[0]), int(robot[1])), (int(robot[2]), int(robot[3]))])
    return robots

def display_robots(robots, room_size):
    c = Counter()
    for robot in robots:
        c[robot[0]] += 1
    for y in range(room_size[1]):
        line = ''.join(map(str, [c[(x, y)] for x in range(room_size[0])]))
        print(re.sub(r'[0]', '.', line))

def solve_part_a(input_data):
    robots = parse_data(input_data)
    room_size = (101, 103)

    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0
    for robot in robots:
        robot[0] = vector_modulo(vector_add(robot[0], vector_multiply(robot[1], 100)), room_size)
        if robot[0][0] < (room_size[0] - 1) / 2 and robot[0][1] < (room_size[1] - 1) / 2:
            quadrant_1 += 1
        if robot[0][0] > (room_size[0] - 1) / 2 and robot[0][1] < (room_size[1] - 1) / 2:
            quadrant_2 += 1
        if robot[0][0] < (room_size[0] - 1) / 2 and robot[0][1] > (room_size[1] - 1) / 2:
            quadrant_3 += 1
        if robot[0][0] > (room_size[0] - 1) / 2 and robot[0][1] > (room_size[1] - 1) / 2:
            quadrant_4 += 1

    print(quadrant_1, quadrant_2, quadrant_3, quadrant_4)
    return (quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4)




def solve_part_b(input_data):
    robots = parse_data(input_data)
    room_size = (101, 103)

    for seconds in range(10403):
        robots = parse_data(input_data)
        quadrant_1 = 0
        quadrant_2 = 0
        quadrant_3 = 0
        quadrant_4 = 0
        tree = 0
        for robot in robots:
            robot[0] = vector_modulo(vector_add(robot[0], vector_multiply(robot[1], seconds)), room_size)
            if robot[0][0] < (room_size[0] - 1) / 2 and robot[0][1] < (room_size[1] - 1) / 2:
                quadrant_1 += 1
            if robot[0][0] > (room_size[0] - 1) / 2 and robot[0][1] < (room_size[1] - 1) / 2:
                quadrant_2 += 1
            if robot[0][0] < (room_size[0] - 1) / 2 and robot[0][1] > (room_size[1] - 1) / 2:
                quadrant_3 += 1
            if robot[0][0] > (room_size[0] - 1) / 2 and robot[0][1] > (room_size[1] - 1) / 2:
                quadrant_4 += 1
            if (2*robot[0][0] + robot[0][1] > room_size[0]) and (2*(room_size[0]-robot[0][0]) + robot[0][1] > room_size[0]):
                #sort of a triangle shape, from top middle to each bottom corner
                tree += 1

        if tree > 390:
            display_robots(robots, room_size)
            print(seconds, quadrant_1, quadrant_2, quadrant_3, quadrant_4, tree)
            return seconds


if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    #print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example data: {example_data_a}')
    # print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    # print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')