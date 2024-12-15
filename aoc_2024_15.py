import re
from collections import deque
from pprint import pprint

from aocd import get_puzzle
from parse import parse

YEAR = 2024
DAY = 15

example_data_a = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''
example_data_b = example_data_a

direction_map = {'<':(-1, 0), '>':(1, 0), '^':(0,-1), 'v':(0, 1)}
room_map = []
robot_location = None
move_queue = deque()

def vector_add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def parse_data(input_data):
    robot_location = None
    split_data = input_data.split('\n\n')
    room_map = [list(line) for line in split_data[0].splitlines()]
    movements = ''.join(split_data[1].splitlines())

    for y, row in enumerate(room_map):
        for x, space in enumerate(row):
            if space == '@':
                robot_location = (x, y)

    return room_map, movements, robot_location

def parse_data_wide(input_data):
    robot_location = None
    split_data = input_data.split('\n\n')
    room_data = split_data[0]
    room_data = re.sub(r'#', '##', room_data)
    room_data = re.sub(r'O', '[]', room_data)
    room_data = re.sub(r'\.', '..', room_data)
    room_data = re.sub(r'@', '@.', room_data)
    room_map = [list(line) for line in room_data.splitlines()]
    movements = ''.join(split_data[1].splitlines())

    for y, row in enumerate(room_map):
        for x, space in enumerate(row):
            if space == '@':
                robot_location = (x, y)

    return room_map, movements, robot_location

def gps(map):
    total = 0
    for y, row in enumerate(map):
        for x, space in enumerate(row):
            if space == 'O' or space == '[':
                total += 100*y + x

    return total

def queue_move(object_location, target_location):
    if (object_location, target_location) not in move_queue:
        move_queue.append(((object_location), (target_location)))

def clear_queue():
    move_queue.clear()

def resolve_queue():
    while move_queue:
        object_location, target_location = move_queue.popleft()
        object = room_map[object_location[1]][object_location[0]]
        room_map[target_location[1]][target_location[0]] = object
        room_map[object_location[1]][object_location[0]] = '.'

def move(object_location, direction):
    object = room_map[object_location[1]][object_location[0]]
    target_location = vector_add(object_location, direction)
    target_object = room_map[target_location[1]][target_location[0]]
    if target_object == '#':
        return False
    if target_object == 'O':
        if not move(target_location, direction):
            return False
    if target_object in '[]':
        if direction in [(0, 1), (0, -1)]: #up and down
            if not move(target_location, direction):
                return False
            if target_object == '[':
                if not move(vector_add(target_location, (1, 0)), direction):
                    return False
            else:
                if not move(vector_add(target_location, (-1, 0)), direction):
                    return False
        else:
            if not move(target_location, direction):
                return False

    queue_move(object_location, target_location)
    if object == '@':
        resolve_queue()
        global robot_location
        robot_location = target_location
    return True


def solve_part_a(input_data):
    global room_map, robot_location
    room_map, movements, robot_location = parse_data(input_data)

    for movement in movements:
        direction = direction_map[movement]
        if not move(robot_location, direction):
            clear_queue()

    return gps(room_map)


def solve_part_b(input_data):
    global room_map, robot_location
    room_map, movements, robot_location = parse_data_wide(input_data)

    for movement in movements:
        direction = direction_map[movement]
        if not move(robot_location, direction):
            clear_queue()

    return gps(room_map)

if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example data: {example_data_a}')
    print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    # print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')