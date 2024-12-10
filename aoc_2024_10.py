from aocd import get_puzzle
from pprint import pprint

YEAR = 2024
DAY = 10

example_data_a = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
example_data_b = example_data_a

class TrailNode():
    def __init__(self, location, value):
        self.location = location
        self.value = int(value)
        self.parents = []
        self.children = []

    def __repr__(self):
        return f"{self.location} [{self.value}]\nParents: {[parent.location for parent in self.parents]}\nChildren: {[child.location for child in self.children]}"

def parse_data(input_data):
    trail_map = [list(line) for line in input_data.splitlines()]
    node_map = {}

    for y in range(len(trail_map)):
        for x in range(len(trail_map[0])):
            new_node = TrailNode((x, y), trail_map[y][x])
            node_map[new_node.location] = new_node

    for current_node in node_map.values():
        north = (current_node.location[0], current_node.location[1]-1)
        west = (current_node.location[0]-1, current_node.location[1])
        east = (current_node.location[0]+1, current_node.location[1])
        south = (current_node.location[0], current_node.location[1]+1)
        for direction in [north, west, east, south]:
            if neighbour := node_map.get(direction, None):
                if neighbour.value == current_node.value+1:
                    current_node.children.append(neighbour)
                    neighbour.parents.append(current_node)

    return node_map

def trail_search(current_node):
    found = set()
    if current_node.value == 9:
        found.add(current_node.location)
        return found
    for node in current_node.children:
        found.update(trail_search(node))
    return found

def trail_search_b(current_node):
    found = []
    if current_node.value == 9:
        found.append(current_node.location)
        return found
    for node in current_node.children:
        found.extend(trail_search_b(node))
    return found

def solve_part_a(input_data):
    node_map = parse_data(input_data)

    trailheads = [node for node in node_map.values() if node.value == 0]
    return sum([len(trail_search(trailhead)) for trailhead in trailheads])

def solve_part_b(input_data):
    node_map = parse_data(input_data)

    trailheads = [node for node in node_map.values() if node.value == 0]
    return sum([len(trail_search_b(trailhead)) for trailhead in trailheads])

if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example data: {example_data_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_a}')
    print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    print()
    print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')