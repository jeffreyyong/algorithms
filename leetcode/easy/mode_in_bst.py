'''
Given a binary search tree (BST) with duplicates, find all the modes(s) in the given BST.
Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key
- Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: if a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? 
(Assume that the implicit stack space incurred due to recursion does not count).
'''

'''
Solution:

I've seen several solutions claimed to be O(1) space. but I disagree. They traverse the tree in-order and keep
track of the current set of modes (among other things). But that's not O(1) space, not even when disregarding
recursion stack space (as explicitly allowed in this question) and result space (not mentioned but reasonable)

The set's contents aren't on stack space, so it can't be disregarded that way. And if the values for example 
1,2,3,4,....,n-2,n-1,n-1 (unique values followed by one double value), the set grows to Omega(n) and it can't be 
disregarded because the result only has 1 size.

I think the way to do it properly is to do two passes. One to find the highest number of occurrences of any value,
and then a second pass to collect all values occurring that often. Any other ideas?

Here's a two-pass solution that I can think can rightfully be called O(1) space. Both passes keep track of the current
value etc, and the second pass additionally collects the modes in the result array. I took the value handling out of the
in-order traversal into its own function for clarity. Also, this way you could very easily replace my recursive
in-order traversal with for example Morris traversal. Then you woulnd't even need to disregard the recursion stack
space in order to claim O(1) extra spoace usage.
'''
