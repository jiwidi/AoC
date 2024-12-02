from itertools import combinations
from math import prod


def read_input(path):
    return [int(x) for x in open(path)]


def find_combination(amount_of_entries):
    entries = read_input("input1.txt")
    for combination in combinations(entries, amount_of_entries):
        if sum(combination) == 2020:
            return prod(combination)


print(find_combination(2))
print(find_combination(3))
