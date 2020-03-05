"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6

YACHT = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    dict_dice, set_dice = dicelist_dict_set(dice)
    if category == ONES or category == TWOS or category == THREES \
            or category == FOURS or category == FIVES or category == SIXES:
        return category * dict_dice[category]
    elif category == YACHT:
        if len(set_dice) == 1:
            return 50
        return 0
    elif category == FULL_HOUSE:
        if len(set_dice) != 2:
            return 0
        s = 0
        for i in set_dice:
            if dict_dice[i] == 2 or dict_dice[i] == 3:
                s += dict_dice[i] * i
            else:
                return 0
        return s
    elif category == FOUR_OF_A_KIND:
        if len(set_dice) != 2 and len(set_dice) != 1:
            return 0
        if dict_dice[dice[1]] >= 4:
            return dice[1] * 4
        else:
            return 0
    elif category == LITTLE_STRAIGHT:
        for i in range(5):
            if dice[i] != i+1:
                return 0
        return 30
    elif category == BIG_STRAIGHT:
        for i in range(5):
            if dice[i] != i+2:
                return 0
        return 30
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0


def dicelist_dict_set(dice):
    dict_dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    dice.sort()
    for value in dice:
        dict_dice[value] += 1
    return dict_dice, set(dice)
