def validate_line(line):
    diffs = [line[i] - line[i - 1] for i in range(1, len(line))]

    return all([0 < diff < 4 for diff in diffs]) or all(
        [0 > diff > -4 for diff in diffs]
    )


def part_one(input):
    return sum([validate_line(line) for line in input])


def part_two(input):
    return sum(
        any(validate_line(line[:i] + line[i + 1 :]) for i in range(len(line) + 1))
        for line in input
    )


def parse_input(input_path):
    input_raw = open(input_path, "r").readlines()
    input_raw = [[int(i) for i in line.split()] for line in input_raw]
    return input_raw


def main():
    input = parse_input("input.txt")
    print("Part 1: ", part_one(input))
    print("Part 2: ", part_two(input))


if __name__ == "__main__":
    main()
