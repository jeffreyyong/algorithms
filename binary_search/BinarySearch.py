# Iterative verion of binary_search

def binary_search(target, nums):

    floor = -1
    ceiling = len(nums)

    while floor + 1 < ceiling:
        distance = ceiling - floor
        half_distance = distance / 2
        guess_index = floor + half_distance

        guess_value = nums[guess_index]

        if guess_value == target:
            return True

        if guess_value > target:
            ceiling = guess_index

        else:
            floor = guess_index

    return False

# How did we know the time cost of binary search was O(lgn). The only non-constant part 
# of our time costs is the number of times our while loop runs. 
# Each step of our while loop cuts the range 
# 


        

