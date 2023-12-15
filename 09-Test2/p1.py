def card_value(card):
    """Function to determine the value of a card."""
    if card in ['A', 'K', 'Q', 'J', 'T']:
        return 10
    else:
        return int(card)

def compare_players(player1, player2):
    """Function to compare the values of cards for two players."""
    value_player1 = sum(card_value(card) for card in player1)
    value_player2 = sum(card_value(card) for card in player2)

    return value_player1 >= value_player2

# Example usage:
player1_hand = ['A', 'K', '7', '8']
player2_hand = ['Q', 'J', 'T', '9']

result = compare_players(player1_hand, player2_hand)

if result:
    print("Player 1 has cards of the same or higher value.")
else:
    print("Player 2 has cards of higher value.")