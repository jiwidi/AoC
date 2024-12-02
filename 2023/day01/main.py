import inflect


def create_num_dict(start, end):
    p = inflect.engine()
    num_dict = {}

    for i in range(start, end + 1):
        word = p.number_to_words(i)
        num_dict[word] = word[0] + str(i) + word[-1]

    return num_dict


def puzzle_one(input_text):
    count = 0
    for line in input_text:
        line = "".join([i for i in line if i.isdigit()])
        calibration_value = int(f"{line[0]}{line[-1]}")
        count += calibration_value
    return count


def puzzle_two(input_text):
    digit_str = create_num_dict(1, 100)
    for i, line in enumerate(input_text):
        for key, value in digit_str.items():
            line = line.replace(key, value)
        input_text[i] = line
    return puzzle_one(input_text)


def main():
    input_text = open("input.txt", "r").readlines()
    print("Solution for puzzle one", puzzle_one(input_text))
    print("Solution for puzzle two", puzzle_two(input_text))


if __name__ == "__main__":
    main()
