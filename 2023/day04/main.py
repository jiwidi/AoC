def read_input():
    with open("input.txt") as f:
        content = f.readlines()
    cards = []
    for line in content:
        line = line.split(":")[1].strip()
        card = line.split("|")
        winning_numbers = [int(x) for x in card[0].strip().split()]
        owned_numbers = [int(x) for x in card[1].strip().split()]
        cards.append([winning_numbers, owned_numbers])

    return cards


def puzzle_one(cards):
    card_points = []
    for card in cards:
        winning_cards = 0
        winning_numbers = card[0]
        owned_numbers = card[1]
        for number in owned_numbers:
            if number in winning_numbers:
                winning_cards += 1
        if winning_cards == 0:
            card_points.append(0)
        else:
            card_points.append(2 ** (winning_cards - 1))

    return sum(card_points)


def puzzle_two(cards):
    gained_cards = len(cards)
    cards = [[i, card] for i, card in enumerate(cards)]

    # First pass to cache what cards does each card give.
    card_earnings = {}
    for card in cards:
        i = card[0]
        card = card[1]
        winning_cards = 0
        winning_numbers = card[0]
        owned_numbers = card[1]
        cards_to_earn = []
        for number in owned_numbers:
            if number in winning_numbers:
                winning_cards += 1
        for j in range(winning_cards):
            new_card_index = i + j + 1
            cards_to_earn.append(cards[new_card_index])
        card_earnings[i] = cards_to_earn

    # Use cache to solve all cards.
    while len(cards) > 0:
        first_element = cards.pop(0)
        i = first_element[0]
        cards_to_earn = card_earnings[i]
        gained_cards += len(cards_to_earn)
        cards = cards_to_earn + cards

    return gained_cards


def main():
    content = read_input()
    print(puzzle_one(content))
    print(puzzle_two(content))


if __name__ == "__main__":
    main()
