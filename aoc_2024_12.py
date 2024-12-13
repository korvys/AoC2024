from collections import deque
from itertools import count
from pprint import pprint

from aocd import get_puzzle

YEAR = 2024
DAY = 12

example_data_a = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
example_data_b = example_data_a

class Region():
    region_id_counter = count()
    def __init__(self, plant):
        self.region_id = next(Region.region_id_counter)
        self.plant = plant
        self.plots = []
        self.fences = []

    def __repr__(self):
        return f"{self.region_id} [{self.plant}] A:{self.area()}, P:{self.perimeter()}, S:{self.sides()} - {self.plots}"

    def area(self):
        return len(self.plots)

    def calculate_fences(self):
        for plot in self.plots:
            north = (plot[0], plot[1] - 1)
            west = (plot[0] - 1, plot[1])
            east = (plot[0] + 1, plot[1])
            south = (plot[0], plot[1] + 1)
            if north not in self.plots:
                self.fences.append(((plot), 'N'))
            if west not in self.plots:
                self.fences.append(((plot), 'W'))
            if south not in self.plots:
                self.fences.append(((south), 'S'))
            if east not in self.plots:
                self.fences.append(((east), 'E'))

    def perimeter(self):
        done_list = []
        perimeter = 0
        for plot in self.plots:
            perimeter += 4
            north = (plot[0], plot[1] - 1)
            west = (plot[0] - 1, plot[1])
            east = (plot[0] + 1, plot[1])
            south = (plot[0], plot[1] + 1)
            adjacent = sum([1 for direction in [north, south, east, west] if direction in done_list])
            perimeter -= 2*adjacent
            done_list.append(plot)
        return perimeter

    def sides(self):
        if not self.fences:
            self.calculate_fences()
        fences_to_check = self.fences[:]
        sides = []

        while fences_to_check:
            side = []
            fence = fences_to_check.pop(0)
            side.append(fence)
            fence_queue = deque()
            if fence[1] == 'N':
                west = ((fence[0][0] - 1, fence[0][1]), 'N')
                east = ((fence[0][0] + 1, fence[0][1]), 'N')
                fence_queue.extend([west, east])
            if fence[1] == 'W':
                north = ((fence[0][0], fence[0][1] - 1), 'W')
                south = ((fence[0][0], fence[0][1] + 1), 'W')
                fence_queue.extend([north, south])
            if fence[1] == 'S':
                west = ((fence[0][0] - 1, fence[0][1]), 'S')
                east = ((fence[0][0] + 1, fence[0][1]), 'S')
                fence_queue.extend([west, east])
            if fence[1] == 'E':
                north = ((fence[0][0], fence[0][1] - 1), 'E')
                south = ((fence[0][0], fence[0][1] + 1), 'E')
                fence_queue.extend([north, south])
            while fence_queue:
                fence = fence_queue.popleft()
                if fence in side:
                    continue
                if fence not in fences_to_check:
                    continue
                if fence[1] == 'N':
                    west = ((fence[0][0] - 1, fence[0][1]), 'N')
                    east = ((fence[0][0] + 1, fence[0][1]), 'N')
                    fence_queue.extend([west, east])
                if fence[1] == 'W':
                    north = ((fence[0][0], fence[0][1] - 1), 'W')
                    south = ((fence[0][0], fence[0][1] + 1), 'W')
                    fence_queue.extend([north, south])
                if fence[1] == 'S':
                    west = ((fence[0][0] - 1, fence[0][1]), 'S')
                    east = ((fence[0][0] + 1, fence[0][1]), 'S')
                    fence_queue.extend([west, east])
                if fence[1] == 'E':
                    north = ((fence[0][0], fence[0][1] - 1), 'E')
                    south = ((fence[0][0], fence[0][1] + 1), 'E')
                    fence_queue.extend([north, south])
                side.append(fence)
                fences_to_check.remove(fence)
            sides.append(side)

        return len(sides)

    def price(self):
        return self.area()*self.perimeter()

    def discount_price(self):
        return self.area()*self.sides()

def parse_data(input_data):
    garden_map = [list(line) for line in input_data.splitlines()]
    garden_map_size = (len(garden_map[0]), len(garden_map))
    garden_plots = [(x, y) for x in range(len(garden_map[0])) for y in range(len(garden_map))]

    regions = []

    while garden_plots:
        starting_plot = garden_plots.pop(0)
        region = Region(garden_map[starting_plot[1]][starting_plot[0]])
        region.plots.append(starting_plot)
        north = (starting_plot[0], starting_plot[1] - 1)
        west = (starting_plot[0] - 1, starting_plot[1])
        east = (starting_plot[0] + 1, starting_plot[1])
        south = (starting_plot[0], starting_plot[1] + 1)
        plot_queue = deque([north, south, east, west])
        while plot_queue:
            plot = plot_queue.popleft()
            if not ((0 <= plot[0] < garden_map_size[0]) and (0 <= plot[1] < garden_map_size[1])):
                continue
            if plot in region.plots:
                continue
            if garden_map[plot[1]][plot[0]] != region.plant:
                continue
            north = (plot[0], plot[1] - 1)
            west = (plot[0] - 1, plot[1])
            east = (plot[0] + 1, plot[1])
            south = (plot[0], plot[1] + 1)
            plot_queue.extend([north, south, east, west])
            region.plots.append(plot)
            garden_plots.remove(plot)
        regions.append(region)


    return regions


def solve_part_a(input_data):
    regions = parse_data(input_data)
    pprint(regions)
    return sum([region.price() for region in regions])

def solve_part_b(input_data):
    regions = parse_data(input_data)
    pprint(regions)
    return sum([region.discount_price() for region in regions])

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