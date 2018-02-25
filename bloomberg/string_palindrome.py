'''
A palindromic string is when all the nonalphanumeric are removed it reads the same front to back ignoring case.
For example, "A man a plan, a canal, Panama". and "Able was I, ere I saw Elba!" are palindromic, but "Ray a Ray"is not

Implement a function which takes as input a string s and returns true if s is a palindromic string.
'''

'''
A naive approach is to create a reversed version of s, and compare it with s, skipping nonalphanumeric characters. This requires
additional space proportional to the length of s.

Do not need to create the reverse - rather, can get the effect of the reverse of s by traversing from right to left. Specifically, 
use two indices to traverse the string, one forward, and the other backwards, skiping non alphanumeric characters, performing
case-insensitive comparison on the alphanumeric characters. Return false as soon as there is a mismatch. If the indices
cross, we have verified palindromicity.

Classis two pointer method which is only O(n) in time complexity
'''

def solution(s):
    # i moves forward, and j moves backward.
    i, j = 0, len(s) - 1
    # i an j both skip non-alphanumeric characters.
    while not s[i].isalnum() and i < j:
        i += 1

    while not s[j].isalnum() and i < j:
        j -= 1

    if s[i].lower() != s[j].lower():
        return False

    i, j = i + 1, j - 1

    return True
