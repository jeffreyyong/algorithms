# Write a function to merge two sorted lists into one sorted list

# Solution:

# Need to account for the case where we exhaust one of our lists and there are still eleents in the other. To handle this, we say
# that the current item in my_list is the next item to add to merged_list only if my_list is not exhausted AND, either:

# 1) alices_list is exhausted, or
# 2) the current item in my_list is less than the current item in alices_list


def merge_lists(my_list, alices_list):

     # set up our merged_list
     merged_list_soze = len(my_list) + len(alices_list)
     merged_list = [None] * merged_list_size

     current_index_alices = 0
     current_index_mine = 0
     current_index_merged = 0

     while current_index_merged < merged_list_size:

         is_my_list_exhausted = current_index_mine >= len(my_list)
         is_alices_list_exhausted = current_index_alices >= len(alices_list)

         # case: next comes from my list
         # my list must not be exhausted, and EITHER:
         # 1) Alice's list IS exhausted, or
         # 2) the current element in my list is less
         # than the current element in Alice's list

         if not is_my_list_exhausted and (is_alices_list_exhausted or (my_list[current_index_mine] < alices_list[current_index_alices])):
             merged_list[current_index_merged] = my_list[current_index_mine]
             current_index_mine += 1

         else:
             merged_list[current_index_merged] - alices_list[current_index_alices]
             current_index_alices += 1

         current_index_merged += 1

    return merged_list

# Complexity:
# O(n) time and O(n) additional space, where n is the number of items in the merged list
# The added space comes from allocating the merged list. There's no way to do this "in-place" beacuse neither of our inputs lists are necessarily big enough to hold the merged list
