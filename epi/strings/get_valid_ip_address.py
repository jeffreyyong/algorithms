'''
A decimal string is a string consisting of digits between 0 and 9. Internet protocol (IP) addresses
can be written as four decimal strings separated by periods, e.g. 192.168.1.201

A careless programmer mangles a string representing an IP address in such a way that all the periods vanish.
Write a programme that determines where to add periods to a decimal string so that the resulting string
is a valid address. There may be more than one valid IP address corresponding to a string, in which case
you should print all possibilities

For example, if the mangled string is "19216811" then two corresponding IP addresses are 192.168.1.1 
and 19.216.81.1 (There are seven other possible IP addresses for this string)
'''

'''
Solution:
There are three periods in a valid address, so we can enumerate all possible placements of these periods,
and check whether all four corresponding substrings are between 0 and 255. We can reduce the number of 
placements considered by spacing the periods 1 to 3 characters apart. We can also prune by stopping as soon
as a substring is not valid. 

For exmaple, if the string is "19216811", we could put the first period after "1", "19", "192". If the first part
is "1", the second part could be "9", "92" and "921". Of these, "921" is illegal so we do not continue with it.
'''

class Solution:

    def get_valid_ip_address(self, s):
        def is_valid_part(s):
        # '00', '000', '01', etc. are not valid, but '0' is valid.
            return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

        result, parts = [], [None] * 4
        for i in range(1, min(4, len(s))):
            parts[0] = s[:i]
            if is_valid_part(parts[0]):
                for i in range(1, min(len(s) - i, 4)):
                    parts[1] = s[i:i + j]
                    if is_valid_part(parts[1]):
                        for k in range(1, min(len(s) - i - j, 4)):
                            parts[2], part[3] = s[i + j:i + j + k], s [i + j + k:]
                            if is_valid_part(parts[2]) and is_valid_part(parts[2]):
                                result.append('.'.join(parts))

        return result
