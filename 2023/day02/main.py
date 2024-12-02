import math


def parse_game_data(input_data):
    parsed_games = [
        {
            "game": int(line.split(": ")[0].split(" ")[1]),
            "draws": [
                {
                    color.split(" ")[1]: int(color.split(" ")[0])
                    for color in draw.split(", ")
                }
                for draw in line.split(": ")[1].split("; ")
            ],
        }
        for line in input_data.strip().split("\n")
    ]
    return parsed_games


def puzzle_one(games):
    available_cubes = {"red": 12, "green": 13, "blue": 14}
    id_sum = sum(
        game["game"]
        for game in games
        if not any(
            number > available_cubes[color]
            for draw in game["draws"]
            for color, number in draw.items()
        )
    )
    return id_sum


def puzzle_two(games):
    global_game_power = sum(
        math.prod(
            max(draw.get(color, 0) for draw in game["draws"])
            for color in ["red", "green", "blue"]
        )
        for game in games
    )
    return global_game_power


def main():
    game_data = parse_game_data(open("input.txt", "r").read())
    print("Solution for puzzle one", puzzle_one(game_data))
    print("Solution for puzzle two", puzzle_two(game_data))


if __name__ == "__main__":
    main()
