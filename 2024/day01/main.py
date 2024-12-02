from collections import defaultdict


def part_one(first_list, second_list):
    first_list = sorted(first_list)
    second_list = sorted(second_list)
    r = 0
    for a, b in zip(first_list, second_list):
        r += abs(a - b)
    return r


def part_two(first_list, second_list):
    # a dict that defaults to value 0
    count_dict = defaultdict(lambda: 0)
    for i in second_list:
        count_dict[i] += 1

    return sum([i * count_dict[i] for i in first_list])


def parse_input(input_path):
    input_raw = open(input_path, "r").readlines()
    first_list = []
    second_list = []
    for i in input_raw:
        first_list.append(int(i.split()[0]))
        second_list.append(int(i.split()[1]))
    return first_list, second_list


def main():
    first_list, second_list = parse_input("input.txt")
    print("Part 1: ", part_one(first_list, second_list))
    print("Part 2: ", part_two(first_list, second_list))


if __name__ == "__main__":
    main()
