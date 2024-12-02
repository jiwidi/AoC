def calc_next(position, grid, slope_x, slope_y):
    size_x = len(grid[0])
    size_y = len(grid)
    if (position[0] + slope_x) < size_x:
        return [position[0] + slope_x, position[1] + slope_y]
    else:
        return [slope_x - (size_x - position[0]), position[1] + slope_y]


def calc_trees(grid, slope_x, slope_y):
    size_y = len(grid)
    position = [0, 0]
    tree_counter = 0
    while position[1] < size_y:
        if grid[position[1]][position[0]] == "#":
            tree_counter += 1
        position = calc_next(position, grid, slope_x, slope_y)
    return tree_counter


def read_input(path="input.txt"):
    return [x.rstrip("\n") for x in open(path)]


if __name__ == "__main__":
    grid = read_input("input.txt")
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    r = [calc_trees(grid, x[0], x[1]) for x in slopes]
    print("Problem 1", r[1])
    product = 1
    for x in r:
        product *= x
    print("Problem 2", product)
