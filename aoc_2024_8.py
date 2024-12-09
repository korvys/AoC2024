from collections import defaultdict
from itertools import combinations

from aocd import get_puzzle

YEAR = 2024
DAY = 8

example_data_a = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
example_data_b = example_data_a

def generate_primary_antinodes(antenna_pair):
    location1, location2 = antenna_pair
    vector = (location2[0] - location1[0], location2[1] - location1[1])
    antinode1 = (location1[0] - vector[0], location1[1] - vector[1])
    antinode2 = (location2[0] + vector[0], location2[1] + vector[1])

    return [antinode1, antinode2]

def generate_complete_antinodes(antenna_pair, map_size):
    location1, location2 = antenna_pair
    vector = (location2[0] - location1[0], location2[1] - location1[1])
    forward_antinodes = []
    backward_antinodes = []

    multiple = 0
    while(True):
        antinode = (location2[0] + vector[0] * multiple, location2[1] + vector[1] * multiple)
        if (0 <= antinode[0] < map_size[0]) and (0 <= antinode[1] < map_size[1]):
            forward_antinodes.append(antinode)
        else:
            break
        multiple += 1

    multiple = 0
    while(True):
        antinode = (location1[0] - vector[0] * multiple, location1[1] - vector[1] * multiple)
        if (0 <= antinode[0] < map_size[0]) and (0 <= antinode[1] < map_size[1]):
            backward_antinodes.append(antinode)
        else:
            break
        multiple += 1

    antinodes = forward_antinodes + backward_antinodes
    return antinodes

def parse_date(input_data):
    map = [list(line) for line in input_data.splitlines()]
    map_size = (len(map[0]), len(map))

    antennas = defaultdict(list)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '.':
                continue
            else:
                antennas[map[y][x]].append((x, y))

    return antennas, map_size

def solve_part_a(input_data):
    antennas, map_size = parse_date(input_data)

    antinodes = set()
    for k, v in antennas.items():
        for antenna_pair in combinations(v, 2):
            antinodes.update(generate_primary_antinodes(antenna_pair))
    antinodes = [antinode for antinode in antinodes if
                 (0 <= antinode[0] < map_size[0]) and (0 <= antinode[1] < map_size[1])]
    print(antinodes)
    return (len(antinodes))



def solve_part_b(input_data):
    antennas, map_size = parse_date(input_data)

    antinodes = set()
    for k, v in antennas.items():
        for antenna_pair in combinations(v, 2):
            antinodes.update(generate_complete_antinodes(antenna_pair, map_size))
    print(antinodes)
    return (len(antinodes))

if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_a}')
    # print(f'Example data: {example_data_a}')
    print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')