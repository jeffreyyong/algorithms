'''
Instructions to candidate
1) Run this code in the REPL to observe its behaviour.l The execution entry point
    is specified at the bottom.
2) Your task is to implement the following function ('longest_uniform_substring').

This function should return a tuple that correctly identifies the location of the 
longest uniform substring within the input string

e.g.

- for the input: "abbbccda" the longest uniform substring is "bbb" (which starts at 
    index 1 and is 3 characters long)
- the tuple returned from the function call would be (1,3)


4) If time permits, try to improve your implementation and add more test cases.
'''

class Solution:

    def longest_uniform_substring(self,input):

        if input == "": return (-1, 0)
        # todo: implement this function
        max_count= 0
        current_count = 0
        start_index = 0
        curr_index = 0

        for x in range(len(input) - 1):
            # check if it is common
            if input[x] == input[x + 1]:
                current_count += 1
            else:
                # reset the counter and find the current_start for recording
                current_start = x
                current_count = 1


            if current_count > max_count:
                start_index = current_start
                max_count = current_count

        return (start_index + 1, max_count)

# def do_tests_pass():
#     '''
#     Returns True if the test passes. Otherwise return False
#     '''

#     # todo: implement more tests
#     test_cases = {
#         "": (-1, 0),
#         "abbbccda": (1, 3),
#         "10000111": (1, 4),
#         "aabbbbbCdAA": (2, 5)
#     }

#     passed = True
#     for input, result in test_cases.items():
#         start, length = longest_uniform_substring(input)
#         passed = passed and start == result[0] and length == result[1]

#     return passed

# if __name__ == "__main__":
#     if do_tests_pass():
#         print("All tests pass!")
#     else:
#         print("At least one failure!")
