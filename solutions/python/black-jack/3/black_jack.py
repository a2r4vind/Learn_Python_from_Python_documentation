"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in {'J', 'Q', 'K'}:
        return 10

    if card == 'A':
        return 1

    if int(card) in range(2,11):
        return int(card)

    return None


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    if card_one_value < card_two_value:
        return card_two
    
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    # getting value of the two cards
    card_one_value, card_two_value = value_of_card(card_one), value_of_card(card_two)
    
    # checking if either card_one or card_two is an Ace ('A') card.
    if card_one == 'A':
        card_one_value = 11
    if card_two == 'A':
        card_two_value = 11
        
    # getting sum of given two card's value
    sum_of_card1_and_card2 = card_one_value + card_two_value

    # getting remaining points 
    remaining_points = 21 - sum_of_card1_and_card2

    return 11 if remaining_points >= 11 else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    given_cards = (card_one, card_two)
    value_10_cards = ('J', 'Q', 'K', '10')
    total = 0

    for card in given_cards:
        value = 0
        if card in value_10_cards:
            value = 10
        elif card == 'A':
            value = 11

        total += value

    return  total == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealtvalue = 0.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    card1_value, card2_value = value_of_card(card_one), value_of_card(card_two)

    return card1_value == card2_value 


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    card1_value, card2_value = value_of_card(card_one), value_of_card(card_two)

    total = card1_value + card2_value

    return  total in (9, 10, 11)
        
