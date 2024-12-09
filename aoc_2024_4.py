from aocd import get_puzzle
from pprint import pprint

YEAR = 2024
DAY = 4

DIRECTIONS = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def check_character(matrix, cursor, character):
    return matrix[cursor[1]][cursor[0]] == character

def check_word(matrix, cursor, word, direction):
    for letter in enumerate(word):
        if not check_character(matrix, (cursor[0]+letter[0]*direction[0], cursor[1]+letter[0]*direction[1]), letter[1]):
            return False
    #print(cursor, direction)
    return True

def check_for_words(matrix, cursor, word='XMAS'):
    found_word_count = 0
    matrix_size = (len(matrix[0]), len(matrix))

    for direction in DIRECTIONS:
        if     (0 <= cursor[0]+(len(word)-1)*direction[0] < matrix_size[0]      # Length of word will stay inbounds: x
            and 0 <= cursor[1]+(len(word)-1)*direction[1] < matrix_size[1]):    # Length of word will stay inbounds: y
            found_word_count += check_word(matrix, cursor, word, direction)

    return found_word_count

def check_for_words_part_2(matrix, cursor):
    found_word_count = 0
    matrix_size = (len(matrix[0]), len(matrix))
    if      cursor[0] == 0 or cursor[0] == matrix_size[0]-1 \
        or  cursor[1] == 0 or cursor[1] == matrix_size[1]-1:
        return 0

    if      ((  check_word(matrix, (cursor[0]-1, cursor[1]-1), 'MAS', (1,1)     )
        or      check_word(matrix, (cursor[0]+1, cursor[1]+1), 'MAS', (-1,-1)   ))
        and  (  check_word(matrix, (cursor[0]+1, cursor[1]-1), 'MAS', (-1,1)    )
        or      check_word(matrix, (cursor[0]-1, cursor[1]+1), 'MAS', (1,-1)    ))):
        return 1
    return 0


def solve_part_a(input_data):
    matrix = [list(line) for line in input_data.splitlines()]
    pprint(matrix)

    total_words = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            count = check_for_words(matrix, (x, y))
            # if count > 0:
            #     print(f"{x},{y}:{count}")
            total_words += count
    print(total_words)
    return total_words

def solve_part_b(input_data):
    matrix = [list(line) for line in input_data.splitlines()]
    pprint(matrix)

    total_words = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            count = check_for_words_part_2(matrix, (x, y))
            # if count > 0:
            #     print(f"{x},{y}:{count}")
            total_words += count
    print(total_words)
    return total_words

if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)
    example_input_data = None
    with open('example_2024_4.txt') as f:
        example_input_data = f.read()

    print('Part 1')
    # print(f'Answered: {puzzle.answered_a}')
    # print(f'Example answer: {puzzle.examples[0].answer_a}')
    print(f'Proposed example answer: {solve_part_a(example_input_data)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    # print()
    # print('Part 2')
    # print(f'Answered: {puzzle.answered_b}')
    # print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b(example_input_data)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')