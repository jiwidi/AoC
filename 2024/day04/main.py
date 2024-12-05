

def part_one(input):
    word = "XMAS"
    max_height = len(input)
    max_width = len(input[0].strip())
    count = 0
    for i in range(max_height):
        for j in range(max_width):
            # To bottom
            if i + len(word) <= max_height:
                s = ''.join(input[i+k][j] for k in range(len(word)))
                if s == word:
                    count +=1
            # To top
            if i - len(word) >= -1:
                s = ''.join(input[i-k][j] for k in range(len(word)))
                if s == word:
                    count +=1
            # To right
            if j + len(word) <= max_width:
                s = ''.join(input[i][j+k] for k in range(len(word)))
                if s == word:
                    count +=1
            # To left
            if j - len(word) >= -1:
                s = ''.join(input[i][j-k] for k in range(len(word)))
                if s == word:
                    count +=1
            # To diagonal bottom-right
            if i + len(word) <= max_height and j + len(word) <= max_width:
                s = ''.join(input[i+k][j+k] for k in range(len(word)))
                if s == word:
                    count +=1
            # To diagonal bottom-left
            if i + len(word) <= max_height and j - len(word) >= -1:
                s = ''.join(input[i+k][j-k] for k in range(len(word)))
                if s == word:
                    count +=1
            # To diagonal top-right
            if i - len(word) >= -1 and j + len(word) <= max_width:
                s = ''.join(input[i-k][j+k] for k in range(len(word)))
                if s == word:
                    count +=1
            # To diagonal top-left
            if i - len(word) >= -1 and j - len(word) >= -1:
                s = ''.join(input[i-k][j-k] for k in range(len(word)))
                if s == word:
                    count +=1
    return count


def part_two(input):
    grid = [line.strip() for line in input]
    max_height = len(grid)
    max_width = len(grid[0])
    count = 0
    for i in range(max_height):
        for j in range(max_width):
            if grid[i][j] == 'A':
                # Check Diagonal1 (top-left to bottom-right)
                if 0 <= i-1 < max_height and 0 <= j-1 < max_width and 0 <= i+1 < max_height and 0 <= j+1 < max_width:
                    diag1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
                    if diag1 == 'MAS' or diag1 == 'SAM':
                        # Check Diagonal2 (top-right to bottom-left)
                        if 0 <= i-1 < max_height and 0 <= j+1 < max_width and 0 <= i+1 < max_height and 0 <= j-1 < max_width:
                            diag2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
                            if diag2 == 'MAS' or diag2 == 'SAM':
                                # Found an X-MAS
                                count += 1
    return count



def parse_input(input_path):
    input_raw = open(input_path, "r").readlines()
    return input_raw


def main():
    input = parse_input("input.txt")
    print("Part 1: ", part_one(input))
    print("Part 2: ", part_two(input))


if __name__ == "__main__":
    main()
