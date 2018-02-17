'''
Two rules that are applied to an array of characters:
1) Replace each 'a' by two 'd's.
2) Delete each entry containing a 'b'.

For example, applying these rules to the array <a,c,d,b,b,c,a> results in the array <d,d,c,d,c,d,d>

Write a program which takes as input an array of characters, and removes each 'b' and replaces each
'a' by two 'd. Specifically, along with the array, you are provided an integer-valued size. Size denotes
the number of entries of the arry that the operation is to be applied to. You do not have to worry about 
preserving subsequent entries. For example, if the array is <a,b,a,c_> and the size is 4, then you can
return <d,d,d,d,c>. You can ssume there is enough space in the array to hold the final result.
'''

'''
Solution:

Library array implementations often have mehtods for inserting into a specific location (all later entries are shifted
right, and the array is resized) and deleting from specific location (all later entries are shifted left, and the size of
the array is decremented). If the input array had such methods, we could apply them - however, the time complexity would be 
O(n^2), wheren is the array's length. The reason is that each insertion and deletion from the array would have O(n) time complexity.

This problem is trivial to solve in O(n) time if we write result to a new array - we skip 'b's, replace 'a's by two 'd's,
and copy over all other characters. However, this entails O(n)additional space

If there are no 'a's, we can implement the function wihout allocating additional space with one forward iteration by skipping 'b's
and copying over the other characters.

If there are no 'b's, we cam implement the function withuot additional space as follows. First, we compute the final length of the
resulting string, which is the length of the array plus the number of 'a's (because number of d's will double). We can then write
the result, character by character, starting from the last character, working our way backwards.

For example, suppose the array is <a,c,a,a,_,_,_> and the specified size is 4. Our algorithm updates the array to 
<a,c,a,a,_,D,D> (Capital denotes the characters that are part of the final result). The next update is <a,c,a,D,D,D,D>, followed by
<a,c,C,D,D,D,D> and finallly <D,D,C,D,D,D,D>

We can combine these two approaches to get a complete algorithm. First we delete 'b's and compute the final number of valid characters
of the string, with a forward iteration through the string. We then replace each 'a' by two 'd's, iterating backwards from the end
of the resulting string. If there are more 'b's than 'a's, the number of valid entries, will decrease, and if there are more 'a's than
'b's, the number will increase. In the programme below we return the number of valid entries in the final result.

The forward and backward iterations each take O(n) time, so the total time complexity is O(n). No additional space is alloweed
'''

class Solution:

    def replace_and_remove(size, s):
        # Forward iteration: remove 'b's and count the number of 'a's
        write_idx, a_count = 0, 0
        for i in range(size):
            if s[i] != 'b':
                s[write_idx] = s[i]
                write_idx += 1

            if s[i] == 'a':
                a_count += 1


        # Backward iteration: replace 'a's with 'dd's starting from the end.

        cur_idx = write_idx - 1
        write_idx += a_count - 1
        final_size = write_idx + 1

        while cur_idx >= 0:
            if s[cur_idx] == 'a':
                s[write_idx - 1:write_idx + 1] = 'dd'
                write_idx -= 2
            else:
                s[write_idx] = s[cur_idx]
                write_idx -= 1

            cur_idx -= 1

        return final_size
