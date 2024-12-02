import re


def check_number_range(value, max_num, min_num):
    if value.isdigit():
        num = int(value)
        return max_num >= num >= min_num
    else:
        return False


def check_byr(value):
    return check_number_range(value, 2002, 1920)


def check_iyr(value):
    return check_number_range(value, 2020, 2010)


def check_eyr(value):
    return check_number_range(value, 2030, 2020)


def check_hgt(value):
    unit = value[-2:]
    if unit == "cm":
        return check_number_range(value[:-2], 193, 150)
    elif unit == "in":
        return check_number_range(value[:-2], 76, 59)
    else:
        return False


def check_hcl(value):
    return bool(re.search("^#[a-f0-9]{6}$", value))


def check_ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(value):
    return len(value) == 9 and value.isdigit()


def check_cid(value):
    return True


value_checkers = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid,
    "cid": check_cid,
}


def extract_passport(passportraw):
    passport_processed = {}
    passportraw = passportraw.replace("\n", " ").strip()
    passportraw = passportraw.split(" ")
    for entry in passportraw:
        key, value = entry.split(":")
        passport_processed[key] = value
    return passport_processed


def check_passport_one(passport):
    # Returns 1 if valid, 0 otherwise
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in required:
        if field not in passport:
            return 0
    return 1


def check_passport_two(passport):
    check_list = []
    if check_passport_one(passport) == 1:
        for key in passport.keys():
            r = value_checkers[key](passport[key])
            check_list.append(r)
        return all(check_list)
    else:
        return False


def read_input(path="input.txt"):
    return open(path).read().split("\n\n")


if __name__ == "__main__":
    passports = read_input("input.txt")
    processed_passports = [extract_passport(passport) for passport in passports]
    r = [check_passport_one(passport) for passport in processed_passports]
    print("Problem 1", sum(r))
    r = [check_passport_two(passport) for passport in processed_passports]
    print("Problem 2", sum(r))
