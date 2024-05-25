from project import initialise_deck
from project import calculate
from project import check
from project import show_hand


def test_initialise_deck():
    assert initialise_deck() == ['A♥', 'A♠', 'A♦', 'A♣', '2♥', '2♠', '2♦', '2♣', '3♥', '3♠', '3♦', '3♣', '4♥', '4♠', '4♦', '4♣',
                                 '5♥', '5♠', '5♦', '5♣', '6♥', '6♠', '6♦', '6♣', '7♥', '7♠', '7♦', '7♣', '8♥', '8♠', '8♦', '8♣',
                                 '9♥', '9♠', '9♦', '9♣', '10♥', '10♠', '10♦', '10♣', 'J♥', 'J♠', 'J♦', 'J♣', 'Q♥', 'Q♠', 'Q♦', 'Q♣',
                                 'K♥', 'K♠', 'K♦', 'K♣']


def test_show_hand():
    assert show_hand(['A♥', 'A♠']) == "Banker's Hand: A♥ _"
    assert show_hand(['4♣', 'A♠', '7♠']) == "Banker's Hand: 4♣ _ _"
    assert show_hand(['7♦', '10♣', '2♠', '8♥']) == "Banker's Hand: 7♦ _ _ _"


def test_calculate():
    assert calculate(['2♦', '2♣']) == 4
    assert calculate(['4♦', '4♣', '7♠']) == 15
    assert calculate(['9♣', '10♥', '5♦']) == 24
    assert calculate(['4♦', '4♣', '7♠', 'A♥']) == 16


def test_check():
    assert check(['2♦', '2♣']) == "Insufficient"
    assert check(['6♦', '8♣', '7♠']) == "Blackjack"
    assert check(['10♣', 'J♥', 'J♠']) == "Bust"