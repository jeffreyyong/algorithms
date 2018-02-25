'''
Calculate the multiplication of every element except the current index

Solution:
To find the products, go through the list greedily twice. First, get the products of all integers before 
each index, and then we go backwards to get the products of all the integers after each index.

When multiply all the products before and after each index, we get our answer - the products of all the integers
except the integer at each index!
'''

def solution(int_list):

    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

    # Make a list with the length of theinput list to hold the products
    result = [None] * len(int_list)

    # For each integer, find the product of all the integers before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(int_list)):
        result[i] = product_so_far
        product_so_far *= int_list[i]


    # For each integer, we find the product of all the integers after it. Since each index in products already has
    # the product of all the integers before i, now we're storing the total product of all other integers
    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        result[i] *= product_so_far
        product_so_far *= int_list[i]


    return result
