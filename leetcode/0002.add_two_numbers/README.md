# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## Question
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

## Thought process
(2 -> 4 -> 3)是 342

(5 -> 6 -> 4)是 465

(7 -> 0 -> 8)是 807

342 + 465 = 807

When dealing with the algorithm, points to care about:
1. Bit additions, need to handle carry problems
2. How to enter the next bit operations
3. After the bitwise addition is completed, it is also necessary to handle the carry problem.
