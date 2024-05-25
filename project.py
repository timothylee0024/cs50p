import random
import sys

# initialising available cards and suit
available_cards = {"number":["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
                    "value":["11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"],}
available_suits = ["♥", "♠", "♦", "♣"]

# initialising common values
max_points = 21
min_points = 17

def main():
    deck = initialise_deck()
    deck, player_hand, banker_hand = initial_hand(deck)
    # Print for extra line between code and start of game
    print()
    print("Your hand:", *player_hand)

    # Check for blackjack
    if check(player_hand) == "Blackjack" and check(banker_hand) == "Blackjack":
        print("You both got Blackjack, it's a tie!")
        game_end(banker_hand)
    elif check(player_hand) == "Blackjack":
        print("Blackjack, you won!")
        game_end(banker_hand)
    elif check(banker_hand) == "Blackjack":
        print("Banker got Blackjack, you lost!")
        game_end(banker_hand)


    # Choice of drawing
    print(show_hand(banker_hand))
    while True:
        print()
        choice = input("Would you like to draw a card (Y/N)? ")
        print()
        # If drawing (hit)
        if choice == "Y":
            yes_choice(deck, player_hand, banker_hand)
        # If staying
        elif choice == "N":
            no_choice(deck, player_hand, banker_hand)


def initialise_deck():
    deck = []
    for card in available_cards["number"]:
        for suit in available_suits:
            deck.append(card + suit)
    return deck


def initial_hand(deck):
    player_cards = 0
    banker_cards = 0
    player_hand = []
    banker_hand = []
    while player_cards < 2 or banker_cards < 2:
        if player_cards > banker_cards:
            draw_card(deck, banker_hand)
            banker_cards += 1
        else:
            draw_card(deck, player_hand)
            player_cards += 1

    return deck, player_hand, banker_hand


def yes_choice(deck, player_hand, banker_hand):
    # Drawing phase:

    # Player's turn
    draw_card(deck, player_hand)
    # Banker's turn
    banker_turn(deck, banker_hand)
    print("Your hand:", *player_hand)
    print(show_hand(banker_hand))

    # Checking phase

    # Win/draw/lose criterias
    if check(player_hand) == "Bust":
        while calculate(banker_hand) < min_points:
            banker_turn(deck, banker_hand)

        if check(banker_hand) == "Bust":
            print("You both busted!")
            game_end(banker_hand)
        else:
            print("You busted, the banker won!")
            game_end(banker_hand)


def no_choice(deck, player_hand, banker_hand):
    if check(player_hand) == "Insufficient":
        print(f"Not enough points, draw more! Current Points: {calculate(player_hand)}. Require: min 16")
        pass
    else:
        # Banker draws until he reaches desired amount
        while calculate(banker_hand) < min_points:
            banker_turn(deck, banker_hand)

        # Checking if banker busted, else run win/draw/lose criterias
        if calculate(banker_hand) > max_points:
            print("Banker busted, You Won! Score:", calculate(player_hand))
            game_end(banker_hand)

        # Win/draw/lose criterias
        if calculate(player_hand) > calculate(banker_hand):
            print("You Won! Score:", calculate(player_hand))
            game_end(banker_hand)
        elif calculate(player_hand) == calculate(banker_hand):
            print("Draw!")
            game_end(banker_hand)
        else:
            print("You Lost! Score:", calculate(player_hand))
            game_end(banker_hand)


def draw_card(deck, hand):
    card = deck.pop(random.randint(0, len(deck)-1))
    hand.append(card)


def show_hand(hand):
    return f"Banker's Hand: {hand[0]}{(len(hand) - 1) * ' _'}"


def calculate(hand):
    i = 0
    points = 0
    num_aces = 0
    while i < len(hand):
        num = available_cards["number"].index(hand[i].rstrip("♥♠♦♣"))
        points = points + int(available_cards["value"][num])
        if int(available_cards["value"][num]) == 11:
            num_aces = num_aces + 1
        i += 1
    # if aces are present, decide if it should be 1 or 11
    while num_aces > 0:
        if points > max_points:
            points = points - 10
        num_aces = num_aces - 1

    return points


def banker_turn(deck, hand):
    if calculate(hand) < min_points:
        draw_card(deck, hand)
    else:
        pass


def check(hand):
    if calculate(hand) > max_points:
        return "Bust"
    elif calculate(hand) == max_points:
        return "Blackjack"
    elif calculate(hand) < min_points:
        return "Insufficient"


def game_end(hand):
    print("Banker's hand:", *hand, "Score:", calculate(hand))
    print()
    sys.exit()


if __name__ == "__main__":
    main()