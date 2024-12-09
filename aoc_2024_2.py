from aocd import get_puzzle

YEAR = 2024
DAY = 2

def parse_data(input_data):
    reports = input_data.splitlines()

    return([list(map(int, report.split())) for report in reports])

def analise_report(report):
    report2 = report[1:]
    comparison = zip(report, report2)
    differences = list(map(lambda l: l[1] - l[0], comparison))
    increasing = list(map(lambda x: x > 0, differences))
    decreasing = list(map(lambda x: x < 0, differences))
    safe = list(map(lambda x: 0 < abs(x) <= 3, differences))
    return comparison, differences, increasing, decreasing, safe

def solve_part_a(input_data):
    reports = parse_data(input_data)
    #print(reports)
    safe_total = 0
    for report in reports:
        comparison, differences, increasing, decreasing, safe = analise_report(report)
        print(report, differences, increasing, decreasing, safe)
        if (all(increasing) or all(decreasing)) and all(safe):
            safe_total += 1

    return safe_total

def solve_part_b(input_data):
    reports = parse_data(input_data)
    #print(reports)
    safe_total = 0
    for report in reports:
        comparison, differences, increasing, decreasing, safe = analise_report(report)
        print(report, differences, increasing, decreasing, safe)
        if (all(increasing) or all(decreasing)) and all(safe):
            safe_total += 1
            continue
        else:
            for i in range(len(report)):
                temp_report = report[:]
                temp_report.pop(i)
                comparison, differences, increasing, decreasing, safe = analise_report(temp_report)
                if (all(increasing) or all(decreasing)) and all(safe):
                    safe_total += 1
                    break
    return safe_total


if __name__ == '__main__':
    puzzle = get_puzzle(day=DAY, year=YEAR)

    print('Part 1')
    print(f'Answered: {puzzle.answered_a}')
    print(f'Example answer: {puzzle.examples[0].answer_a}')
    print(f'Proposed example answer: {solve_part_a(puzzle.examples[0].input_data)}')
    print(f'Proposed final answer: {solve_part_a(puzzle.input_data)}')
    print()
    print('Part 2')
    print(f'Answered: {puzzle.answered_b}')
    print(f'Example answer: {puzzle.examples[0].answer_b}')
    print(f'Proposed example answer: {solve_part_b(puzzle.examples[0].input_data)}')
    print(f'Proposed final answer: {solve_part_b(puzzle.input_data)}')