def check_password_one(password_line):
    policy, letter, password = password_line.split(" ")
    minimum, maximum = policy.split("-")
    minimum = int(minimum)
    maximum = int(maximum)
    letter = letter[0]
    password = password.rstrip("\n")
    count = password.count(letter)
    if count >= minimum and count <= maximum:
        return 1
    return 0


def check_password_two(password_line):
    policy, letter, password = password_line.split(" ")
    minimum, maximum = policy.split("-")
    minimum = int(minimum) - 1
    maximum = int(maximum) - 1
    letter = letter[0]
    password = password.rstrip("\n")
    count = (password[minimum] + password[maximum]).count(letter)
    if count == 1:
        return 1
    return 0


def read_input(path="input.txt"):
    return [x for x in open(path)]


if __name__ == "__main__":
    print(sum([check_password_one(password_line) for password_line in read_input()]))
    print(sum([check_password_two(password_line) for password_line in read_input()]))
