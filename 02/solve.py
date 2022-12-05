# FOE: A for Rock, B for Paper, and C for Scissors.
# Player (part 1): X for Rock, Y for Paper, and Z for Scissors

def get_score_by_choice(choice: str) -> int:
    """
     the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    """
    choices = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    return choices[choice] if choice in choices else 0


def get_outcome_score(foe_choice: str, player_choice: str) -> int:
    """
    the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won
    """

    # FOE + PLAYER as key
    choices = {
        'A': {
            'X': 3,
            'Y': 6,
            'Z': 0
        },
        'B': {
            'X': 0,
            'Y': 3,
            'Z': 6
        },
        'C': {
            'X': 6,
            'Y': 0,
            'Z': 3
        }
    }

    return choices[foe_choice][player_choice]


def choose_figure(foe: str, me: str) -> str:
    """
    X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    """
    choices = {
        'A': {
            'X': 'Z',
            'Y': 'X',
            'Z': 'Y',
        },
        'B': {
            'X': 'X',
            'Y': 'Y',
            'Z': 'Z',
        },
        'C': {
            'X': 'Y',
            'Y': 'Z',
            'Z': 'X',
        }
    }

    return choices[foe][me]


total_score_p1 = 0
total_score_p2 = 0
with open('input.txt') as f:
    for line in f:
        foe, me = line.strip().split(' ')
        total_score_p1 += get_outcome_score(foe, me) + get_score_by_choice(me)

        me_p2 = choose_figure(foe, me)
        total_score_p2 += get_outcome_score(foe, me_p2) + get_score_by_choice(me_p2)

print(f'Part 1: {total_score_p1}')
print(f'Part 2: {total_score_p2}')
