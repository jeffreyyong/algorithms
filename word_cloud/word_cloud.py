# Write code that takeas a long string and buyilds its word cloud data in a dictionary, where the keys are words
# and the values are the number of times the words occurred.

# The final dictionary we return should be the only data structure whose length is tied to n.
# We should only iterate through our input string once.

# We'll have to go through the entire input string, and we're returning a dictionary with every unique word.
# In the worst case every word is different so our runtime and and space cost will both be at least O(n)

class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()

        current_word_start_index = 0
        current_word_length = 0

        for i, character in enumerate(input_string):

            # if we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary

            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                                                current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)

            # if we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary adn reset our current word

            elif character == ' ' or character == u'\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                                                current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0
            # we want to make sure we split on ellipses so if we get two periods in a row
            # we add the current word to our dictionary and reset our current word

            elif character == '.':
                if i < len(input_string) - 1 and input_string[i+1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                                                    current_word_start_index + current_word_length]
                        self.add_word_to_dictinoary(current_word)
                        current_word_length = 0


