from aocd import get_puzzle
from pprint import pprint
from time import perf_counter
import re

YEAR = 2024
DAY = 6

example_data_a = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
example_data_b = example_data_a

def parse_data(input_data):
    map = input_data.splitlines()
    map_size = (len(map[0]), len(map))
    obstructions = []
    for i, line in enumerate(map):
        obj = [m.start() for m in re.finditer('#', line)]
        obstructions.extend([(o, i) for o in obj])
        g = line.find('^')
        if g != -1:
            guard = (g, i, (0, -1))

    return guard, obstructions, map_size

def collide(guard, obstruction):
    direction = guard[2]
    if direction[0] == 0: # Facing vertically
        if guard[0] != obstruction[0]:
            return 0 # Not in the same column
        return (obstruction[1] - guard[1]) * direction[1]
    elif direction[1] == 0:
        if guard[1] != obstruction[1]:
            return 0 # Not in the same column
        return (obstruction[0] - guard[0]) * direction[0]
    else:
        print('Something broke')
        return 0

def make_a_path(point_from, point_to):
    path = []
    if point_from[0] == point_to[0]:
        x = point_from[0]
        if point_from[1] > point_to[1]:
            step = -1
        else:
            step = 1
        for y in range(point_from[1]+step, point_to[1]+step, step):
            path.append((x,y))
    else:
        y = point_from[1]
        if point_from[0] > point_to[0]:
            step = -1
        else:
            step = 1
        for x in range(point_from[0]+step, point_to[0]+step, step):
            path.append((x, y))
    #print(path)
    return path

def move_and_turn(guard, distance):
    direction = guard[2]
    guard_x = guard[0] + distance * direction[0]
    guard_y = guard[1] + distance * direction[1]

    if direction == (0, -1):
        direction = (1, 0)
    elif direction == (1, 0):
        direction = (0, 1)
    elif direction == (0, 1):
        direction = (-1, 0)
    elif direction == (-1, 0):
        direction = (0, -1)
    else:
        print('Something broke in turning')

    visited = make_a_path((guard[0], guard[1]), (guard_x, guard_y))
    guard = (guard_x, guard_y, direction)
    return guard, visited

def run_path(guard, obstructions, map_size):
    visited = set()
    visited.add((guard[0], guard[1]))

    guard_positions = []
    loop = False
    while (True):
        # loop check
        if guard in guard_positions:
            #print("This is a loop!")
            loop = True
            break
        else:
            guard_positions.append(guard)

        move_distance = 0
        for obstruction in obstructions:
            distance = collide(guard, obstruction)
            if distance > 0:
                if move_distance:
                    move_distance = min(distance, move_distance)
                else:
                    move_distance = distance
        if move_distance:
            guard, v = move_and_turn(guard, move_distance - 1)
            visited.update(v)
        else:
            direction = guard[2]
            if direction[0] == 1:
                move_distance = map_size[0] - 1 - guard[0]
            elif direction[0] == -1:
                move_distance = guard[0]
            elif direction[1] == 1:
                move_distance = map_size[1] - 1 - guard[1]
            elif direction[1] == -1:
                move_distance = guard[1]
            guard, v = move_and_turn(guard, move_distance)
            visited.update(v)
            break

    return visited, loop


def solve_part_a(input_data):
    guard, obstructions, map_size = parse_data(input_data)

    visited, loop = run_path(guard, obstructions, map_size)

    return len(visited)


def solve_part_b(input_data):
    guard, obstructions, map_size = parse_data(input_data)

    # Only places that would be visited could cause a loop if an obstruction was added.
    visited, loop = run_path(guard, obstructions, map_size)

    total_loops = 0
    for new_obstruction in visited:
        if new_obstruction in obstructions:
            continue
        obstructions_added = obstructions[:]
        obstructions_added.append(new_obstruction)
        _, loop = run_path(guard, obstructions_added, map_size)
        total_loops += loop

    return total_loops


if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    # print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_a}')
    #print(f'Example data: \n{example_data_a}')
    timer_start = perf_counter()
    print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    timer_stop = perf_counter()
    print(f"Elapsed time: {timer_stop - timer_start}")
    timer_start = perf_counter()
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    timer_stop = perf_counter()
    print(f"Elapsed time: {timer_stop - timer_start}")
    # print()
    # print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_b}')
    timer_start = perf_counter()
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    timer_stop = perf_counter()
    print(f"Elapsed time: {timer_stop - timer_start}")
    timer_start = perf_counter()
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')
    timer_stop = perf_counter()
    print(f"Elapsed time: {timer_stop - timer_start}")