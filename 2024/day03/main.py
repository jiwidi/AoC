import re

def part_one(input):
    pattern = r"\b\w*mul\w*\(\d+,\d+\)"
    matches = re.findall(pattern, input)
    r = 0
    for match in matches:
        numbers = re.search(r"\((\d+),(\d+)\)", match)
        a, b = int(numbers.group(1)), int(numbers.group(2))
        r += a * b
    return r

def part_two(input):
    input = "do()" + input
    tokens = re.split(r"(do\(\)|don't\(\))", input)
    r = 0
    enabled=True
    for token in tokens:
        if token == 'do()':
            enabled = True
        elif token == "don't()":
            enabled = False
        elif enabled:
            r += part_one(token)
    return r


def parse_input(input_path):
    with open(input_path, "r") as file:
        input_raw = file.read()
    return input_raw

def main():
    input = parse_input("input.txt")
    print("Part 1: ", part_one(input))
    print("Part 2: ", part_two(input))

if __name__ == "__main__":
    main()
