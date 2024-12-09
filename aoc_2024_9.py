from aocd import get_puzzle
from itertools import batched, zip_longest
from collections import deque

YEAR = 2024
DAY = 9

example_data_a = '2333133121414131402'
example_data_b = example_data_a


def generate_checksum(files):
    checksum = 0
    files = files[0]
    for i, file in enumerate(files):
        checksum += i * file
    return checksum


def generate_checksum_b(files):
    checksum = 0
    for current_id, v in files.items():
        for i in range(v['position'], v['position']+v['length']):
            checksum += current_id * i
    return checksum


def parse_data(input_data):
    blocks = batched(input_data, 2)
    current_id = 0
    files = deque()
    spaces = deque()
    for block in blocks:
        files.append([current_id]*int(block[0]))
        if len(block) == 2:
            spaces.append(['.']*int(block[1]))
        current_id += 1
    return files, spaces


def parse_data_b(input_data):
    blocks = list(batched(input_data, 2))
    position = 0
    files = {}
    spaces = []
    for current_id in range(len(blocks)):
        files[current_id] = {'position':position, 'length':int(blocks[current_id][0])}
        position += int(blocks[current_id][0])
        if len(blocks[current_id]) == 2:
            spaces.append({'position':position, 'length':int(blocks[current_id][1])})
            position += int(blocks[current_id][1])

    return files, spaces


def solve_part_a(input_data):
    files, spaces = parse_data(input_data)

    while len(files) > 1:
        current_space_block = spaces.popleft()

        new_file_block = []
        required_files = len(current_space_block)
        while required_files > 0 and len(files) > 1:
            current_file_block = files.pop()
            if len(current_file_block) <= required_files:
                new_file_block.extend(current_file_block[::-1])
                required_files -= len(current_file_block)
            else:
                new_file_block.extend(current_file_block[:-(required_files+1):-1])
                current_file_block = current_file_block[:-required_files]
                files.append(current_file_block)
                required_files = 0

        first_file_block = files.popleft()
        if len(files) == 0:
            second_file_block = []
        else:
            second_file_block = files.popleft()
        files.appendleft(first_file_block+new_file_block+second_file_block)
        spaces.append(current_space_block)

    return generate_checksum(files)


def solve_part_b(input_data):
    files, spaces = parse_data_b(input_data)

    max_id = len(files) - 1

    for current_id in range(max_id, -1, -1):
        current_file = files[current_id]
        for space in spaces:
            if space['length'] >= current_file['length'] and space['position'] < current_file['position']:
                new_file = {'position':space['position'], 'length':current_file['length']}
                space['position'] += current_file['length']
                space['length'] -= current_file['length']
                files[current_id] = new_file
                break

    return generate_checksum_b(files)



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
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')