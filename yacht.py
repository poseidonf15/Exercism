"""Module to calculate the score for a given dice throw in the game 'Yacht'."""
# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "fullhouse"
FOUR_OF_A_KIND = "fourofakind"
LITTLE_STRAIGHT = [1,2,3,4,5]
BIG_STRAIGHT = [2,3,4,5,6]
CHOICE = "choice"


def score(dice, category):
    """Function to calculate the score using the target hand with dice throw.

    args:
        dice (list): what came out on the dice
        category: the category of the target hand

    returns:
        int: the score
    """
    if isinstance(category, int):
        return dice.count(category) * category

    if category == "fullhouse":
        if dice.count(min(dice)) == 3 and dice.count(max(dice)) == 2 or dice.count(min(dice)) == 2 and dice.count(max(dice)) == 3:
            return sum(dice)

    if category == "fourofakind":
        if dice.count(min(dice)) >= 4:
            return min(dice) * 4
        if dice.count(max(dice)) >= 4:
            return max(dice) * 4

    if sorted(dice) == category:
        return 30

    if category == "choice":
        return sum(dice)

    if category == "yacht":
        if dice.count(dice[0]) == 5:
            return 50

    return 0