import re
import math


def read_input():
    content = open("input.txt", "r").readlines()
    return content


def puzzle_one_and_two(content):
    found_numbers = []
    for i, line in enumerate(content):
        for match in re.finditer(r"\d+", line):
            number = match.group()
            if number[0] != "0":
                found_numbers.append([i, match.start(), len(number), int(number)])

    def check_range(x, y):
        if x < 0 or y < 0 or x >= len(content) or y >= len(content[x]):
            return 0
        if re.match(r"^\*$", content[x][y]):
            return 2  # Edge case for puzzle two
        if re.match(r"[^\d.\n]", content[x][y]):
            return 1
        return False

    sol = 0
    checked_gears = {}
    for number in found_numbers:
        line = number[0]
        index = number[1]
        length = number[2]
        possible_ranges = (
            [(line - 1, index + i) for i in range(-1, length + 1) if line - 1 >= 0]
            + [(line, index - 1), (line, index + length)]
            + [
                (line + 1, index + i)
                for i in range(-1, length + 1)
                if line + 1 < len(content)
            ]
        )
        valid = False
        for possible_range in possible_ranges:
            check = check_range(*possible_range)
            if check == 2:
                # Check if the gear has list, if so append number otherwise create with number
                checked_gears[possible_range] = checked_gears.get(
                    possible_range, []
                ) + [number[3]]
            valid = valid or check
        if valid:
            sol += number[3]

    # Multiply gears for puzzle 2
    sol_two = 0
    for key, value in checked_gears.items():
        if len(value) > 1:
            gear_ratio = math.prod(value)
            sol_two += gear_ratio
    return sol, sol_two


def main():
    content = read_input()
    one, two = puzzle_one_and_two(content)
    print("Solution for puzzle one", one)
    print("Solution for puzzle two", two)


if __name__ == "__main__":
    main()
