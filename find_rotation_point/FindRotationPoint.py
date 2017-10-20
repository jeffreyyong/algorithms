def find_rotation_point(words):

    first_word = words[0]

    floor = 0
    ceiling = len(words) - 1

    while floor < ceiling:

        guess_index = floor + ((ceiling - floor) / 2)

        if words[guess_index] >= first_word:
            floor = guess_index

        else:
            ceiling = guess_index

        if floor + 1 == ceiling:

            return ceiling


