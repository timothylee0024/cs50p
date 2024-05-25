# Blackjack
![img](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Blackjack21.jpg/640px-Blackjack21.jpg)

#### Video Demo:  <URL HERE>

### Description:

>#### Blackjack is a popular card game that is also known as "21." It is played in casinos around the world and is one of the most widely recognized and enjoyed casino games. The objective of the game is to have a hand with a total value higher than the banker’s without going over 21. Kings, Queens, Jacks and Tens are each worth 10 points, and an Ace has the value of 1 or 11 points. The remaining cards are counted at face value.
>#### Rules of Blackjack:
1. Each player is dealt two cards, whilst the dealer is dealt one faced up
2. If your first 2 cards add up to 21 (an Ace and a card valued 10), that’s Blackjack! If they have any other total, decide whether you wish to ‘draw’ or ‘stay’. Same applies for the banker.
3. Turns are alternated following the order (Player, Banker). The following actions can be taken on each player's turn
    + Draw: Draw a card from the deck
    + Stay: Pass the turn to the next player. All subsequent turns will also be passed.
4. Turns are taken until all players choose to stay. After which, compare the total value of your cards versus the banker. The player with the closest score to 21, without going over wins.
5. Players must draw until they reach a score of 17 or more.


### Project Files:

#### main():
>#### Contains the main logic behind the program. Checks for any initial blackjacks from player and banker, before continuing game based on user input.

#### banker_turn(deck, hand):
>#### Logic behind the banker's decision during his/her turn. If "Points < 17(minimum)", draw. Else, stay.

#### calculate(hand):
>#### Calculates the total number of points of cards.

#### check(hand):
>#### Quantifies corner cases of hand scores and check for bust (score > 21), blackjack (score == 21), or insufficient (score < 17).

#### draw_card(deck, hand):
>#### Draw a card at random from the deck.

#### game_end(hand):
>#### Printed out only at the end of a round. Shows the banker's cards and score.

#### initial_hand():
>#### Gives the player and banker two cards each at random from the deck.

#### initialise_deck():
>#### initialises deck of poker cards (52 cards, from Ace - King for all 4 suits).

#### no_choice(deck, player_hand, banker_hand):
>#### Called if player decides 'stay'. Function will check if player has the minimum required number of points (17) in his/her hand. Function will then prompt banker to draw additional cards if required to satisfy the same requirement. After banker has drawn cards, reveal the cards of both players and print result of the game (Win/Lose).

#### show_hand(hand):
>#### Display's the number of cards in hand with the first card revealed (e.g., "A♦ _ _" indicating first card is A♦ with total 3 cards in hand). This function is used to reveal information about banker's hand similarly to how blackjack is played in real life.

#### yes_choice(deck, player_hand, banker_hand):
>#### Called if player wishes to 'draw' an additional card. After which, function will check if player has busted (points > 21), or can continue playing. If player has busted, check banker's cards and print result of the game (Win/Lose).


### Design Decisions:
- OOP could be used to make a Card object. However, functions were used instead to instantiate the deck (and cards) to better suit the submission and testing criterias.