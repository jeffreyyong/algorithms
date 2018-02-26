'''
Given an array of integers, delete the max and min numbers (both could appear more than once) in place. Do it in O(n)
without shifting
'''

def delete_min_max(array):
    min, max = find_min_max(array)


    return


def find_min_max(A):
    MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)


    if len(A) <= 1:
        return MinMax(A[0], A[0])

    global_min_max = min_max(A[0], A[1])
    # Process two elements at a time.
    for i in range(2, len(A) - 1, 2):
        local_min_max = min_max(A[i], A[i + 1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest))

    # if there is odd number of elements in the arraym we still need to 
    # comprea the last element with the existing answer.
    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )

    return global_min_max

