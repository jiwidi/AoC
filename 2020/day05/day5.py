def decode_row(instructions):
    L = 0
    H = 127
    for instruction in instructions:
        if instruction == "F":
            H = (H - L + 1) // 2 + L - 1
        elif instruction == "B":
            L = (H - L + 1) // 2 + L
    return L


def decode_column(instructions):
    L = 0
    H = 7
    for instruction in instructions:
        if instruction == "L":
            H = (H - L + 1) // 2 + L - 1
        elif instruction == "R":
            L = (H - L + 1) // 2 + L
    return L


def decode_seat(instructions):
    row = decode_row(instructions[:7])
    column = decode_column(instructions[7:])
    return (row * 8) + column


def part_two(seats):
    seats = sorted(seats)
    for idx, seat in enumerate(seats):
        if seats[idx + 1] != (seat + 1):
            return seat + 1


def read_input(path="input.txt"):
    return [x.rstrip("\n") for x in open(path)]


if __name__ == "__main__":
    seats = read_input("input.txt")
    r = [decode_seat(seat) for seat in seats]
    print(max(r))
    r = part_two(r)
    print(r)
