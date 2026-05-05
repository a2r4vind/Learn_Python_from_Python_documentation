"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):

    if list_one == list_two:
        return EQUAL

    def is_sub(small, big):

        if not small: # Empty list is always a sublist
            return True 

        for i in range(len(big) - len(small) + 1):
            if big[i : i + len(small)] == small:
                return True
        return False

    # check list_one is sublist of list_two
    if is_sub(list_one, list_two):
        return SUBLIST

    # check list_one is superlist
    if is_sub(list_two, list_one):
        return SUPERLIST

    return UNEQUAL