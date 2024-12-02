import itertools

def read_input(path):
    inp = [int(line) if line != '' else None for line in open(path).read().splitlines() ]
    inp = [list(g) for k, g in itertools.groupby(inp, key=lambda x: x is None) if not k]
    return inp

def solve(inp):
    total_calories_per_elve = [sum(x) for x in inp]
    solution_part1 = max(total_calories_per_elve)
    sorted_calories = sorted(total_calories_per_elve, reverse=True)
    solution_part2 = sum(sorted_calories[:3])

    return solution_part1, solution_part2

if __name__ == "__main__":
    inp = read_input("input.txt")
    solution_part1, solution_part2 = solve(inp)
    print("Part 1:", solution_part1)
    print("Part 2:", solution_part2)