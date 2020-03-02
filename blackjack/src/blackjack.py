import sys

FACE_CARDS = ['J', 'Q', 'K']


def score_hand(hand):
    '''
    Calculate the total score of the hand.
    '''
    hand_score = 0

    for card in hand:
        if card in FACE_CARDS:
            hand_score += 10
            continue

        if card == 'A':
            hand_score += 1
            if hand_score < 12:
                hand_score += 10
            continue
        try:
            hand_score += int(card)
            continue
        except ValueError:
            print('Invalid card in hand: {}'.format(card))
        except TypeError:
            print('Card is an invalid type: {}'.format(type(card)))
    return hand_score


print(str(score_hand(['A'])))
print(str(score_hand(['5', '4', '3', '2', 'A', 'K'])))
print(str(score_hand(['5', '3', '7'])))
print(str(score_hand(['A', 'J'])))
print(str(score_hand(['A', '10', 'A'])))
