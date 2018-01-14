'''

“Count and Say problem” Write a code to do following:

n  | String to print
___|_________________
0. | 1
1. | 1 1
2. | 2 1
3. | 1 2 1 1
4. | 1 1 1 2 2 1
…
Base case: n = 0 print "1"
for n = 1, look at previous string and write number of times a digit is seen and the digit itself. In this case,

digit 1 is seen 1 time in a row… so print “1 1”

for n = 2, digit 1 is seen two times in a row, so print “2 1”

for n = 3, digit 2 is seen 1 time and then digit 1 is seen 1 so print “1 2 1 1”

for n = 4 you will print “1 1 1 2 2 1”

Consider the numbers as integers for simplicity. e.g. if previous string is “10 1” then 
the next will be “1 10 1 1” and the next one will be “1 1 1 10 2 1”
'''

import itertools

class Solution:
    def count_and_say(self, n):
        s = "1"
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0

            for l in s:
                # if letter is the l, add the counter
                if let == l:
                    count += 1
                # if not, create a temporary string and change let to l
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s
