'''
Given a string, find the first non-repeating character in it. For example, if the
input string is "GeeksforGeeks", then output should be "f" and if input string is 
"GeeksQuiz", then output should be 'G'
'''

'''
Solution:

We can use string characters as index and build a count array. Following is the algorithm
1) Scan the string from left to right and construct the count array.
2) Again, scan the string from left to right and check for count of each character, if
    you find an element whose caount is 1, return it

'''

# Python program to print the first non-repeating character
NO_OF_CHARS = 256

# Returns the array of size 256 containing count of characters
# in the passed char array

def get_char_count_array(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
        return count


# The function returns index of first non-repeating characters in a string.
# If all characters are repeating then returns -1

def first_non_repeating(string):

    count = get_char_count_array(string)
    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    return index
