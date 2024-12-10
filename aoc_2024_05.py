from math import floor

from aocd import get_puzzle

YEAR = 2024
DAY = 5

example_data_a = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
example_data_b = example_data_a

def parse_data(input_data):
    data_lines = input_data.splitlines()
    page_ordering_rules = [rule.split('|') for rule in filter(lambda x: '|' in x, data_lines)]
    #print(page_ordering_rules)
    update_pages = [rule.split(',') for rule in filter(lambda x: ',' in x, data_lines)]
    #print(update_pages)

    return page_ordering_rules, update_pages

def solve_part_a(input_data):
    page_ordering_rules, update_pages = parse_data(input_data)

    middle_page_total = 0
    for update in update_pages:
        before_pages = []
        current_page = None
        after_pages = update[:]

        correct_order = True
        while after_pages and correct_order:
            if current_page:
                before_pages.append(current_page)
            current_page = after_pages.pop(0)

            for rule in page_ordering_rules:
                if not rule[0] in update or not rule[1] in update:
                    continue
                if current_page == rule[1] and not rule[0] in before_pages:
                    correct_order = False

        if correct_order:
            middle_page_total += int(update[floor(len(update)/2)])
        #print(f"Update: {update} - {correct_order}")

    return(middle_page_total)

def solve_part_b(input_data):
    page_ordering_rules, update_pages = parse_data(input_data)

    middle_page_total = 0
    for update in update_pages:
        before_pages = []
        current_page = None
        after_pages = update[:]

        correct_order = True
        while after_pages:
            if current_page:
                before_pages.append(current_page)
            current_page = after_pages.pop(0)

            for rule in page_ordering_rules:
                if not rule[0] in update or not rule[1] in update: # Rule does not apply to this update
                    continue
                if current_page == rule[1] and not rule[0] in before_pages: #If rule is violated, swap pages, reset, and start again
                    correct_order = False
                    i = update.index(rule[0])
                    j = update.index(rule[1])
                    update[i] = rule[1]
                    update[j] = rule[0]

                    before_pages = []
                    current_page = None
                    after_pages = update[:]
                    break

        if not correct_order:
            middle_page_total += int(update[floor(len(update)/2)])
        #print(f"Update: {update}")

    return middle_page_total


if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    print(f'Answered: {puzzle.answered_a}')
    print(f'Example answer: {puzzle.examples[0].answer_a}')
    # print(f'Example data: {example_data_a}')
    print(f'Proposed example answer: {solve_part_a(example_data_a)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    print()
    print('Part 2')
    print(f'Answered: {puzzle.answered_b}')
    # print(f'Example data: {example_data_a}')
    print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b(example_data_b)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')