'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
Implement wildcard pattern matching with support for `?` and `*`.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

'''
Analysis:

For each element in s
If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
If not match, then we check if there is a * previously showed up,
       if there is no *,  return false;
       if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

e.g.

abed
?b*d**

a=?, go on, b=b, go on,
e=*, save * position star=3, save s position ss = 3, p++
e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
d=d, go on, meet the end.
check the rest element in p, if all are *, true, else false;

Note that in char array, the last is NOT NULL, to check the end, use  "*p"  or "*p=='\0'".

'''

class Solution:

    def is_match(self, s, p):
        s_cur, p_cur, match, star = 0, 0, 0, -1

        while s_cur < len(s):
            # Matched the character exactly or matched the single character wild card '?', hence move both pointers
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1

            # matched with the "*" wildcard, but one or many chars may be available
            # Save this *'s position and the matched s position
            elif p_cur < len(p) and p[p_cur] == "*":
                match = s_cur
                star = p_cur
                p_cur += 1


            # There is no match, check if there is a * previously showed up, yes indeed there is
            elif star != -1:
                # set current p to the next element of *
                p_cur = star + 1
                # set current s to the next saved s position
                match += 1
                s_cur = match

            # There is no match, and there is no previous *, so returns false
            else:
                return False

        while p_cur < len(p) and p[p_cur] == "*":
            p_cur += 1

        if p_cur == len(p):
            return True
        else:
            return False
