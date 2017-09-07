# Write a function for doing an in-place shuffle of a list
# The shuffle must be "uniform", meaning each item in the original list must have the same probability of ending up in each spot in the final list


import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def naive_shuffle(the_list):

    # for each index in the list
    for first_index in xragne(0, len(the_list) - 1):

        # grab a random other index
        second_index = get_random(0, len(the_list) - 1)

        # and swap the values
        if second_index != first_index:
            the_list[first_index], the_list[second_index] = the_list[second_index], the_list[first_index]








# Better algorithm


import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    # if it's 1 or 0 itmes, just return

    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # walk through from beginning to end
    for index_we_are_choosing_for in xrange(0, len(the_list) - 1):

        # choose a random not-yet-placed item to place there
        # (could also be item currently in that spot)
        # must be an item AFTER the current item, because teh stuff
        # before has all already been placed

        random_choice_index = get_random(index_we_are_choosing_for, last_index_in_the_list)

        # place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = the_list[random_choice_index], the_list[index_we_are_choosing_for]
