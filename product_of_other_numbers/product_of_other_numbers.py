def main():
    print(get_products_of_all_ints_except_at_index([1,4,7]))

def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise IndexError("Getting the product of numbers at other indices requires at least 2 numbers")

    # we make a list with the length of the input list to hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers before it, storing the total product so far each time

    product_so_far = 1
    i = 0

    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

        # for each integer, we find the product of all the integers after it, since each index in products
        # already has the product of all the integers before it, now we're storing the total product of all 
        # other integers

    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index


if __name__ == "__main__":
    main()

# Complexity
# O(n) time and O(n) space. We make two passes through our input a list, and the list
# we build always has the same length as the input list

# What we learned
# Another question using a greedy approach. The tricky thing about this one: we couldn't actually solve it in one pass
# But we could solve it in two passes

# This approach probably wouldn't have been obvious if we had started off trying to use a greedy approach
# Instaed, we started off by coming up with a slow (but correct) brute forece solution and trying to improve from there

# We looked at what our solution actually calcualted, step by step, and found some repeate work
# Our final answer came from brainstorming ways to avoid doing that repeat work

# So that's a pattern can be applied to other problems:
# Start with a brute force solution, look for repeated work in that situation, and modify it to only do that work once.
