import collections


def solution(integers):
    counter = collections.Counter(integers)

    for i in integers:
        if counter[i] == 1:
            return i
    return 0
