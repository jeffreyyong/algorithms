
def square_list_in_place(int_list):

    # enumerate() lets us get the index and element
    for index, element in enumerate(int_list):
        int_list[index] *= element

    # NOTE: we don't *need* to return anything
    # this is just a convenience
    return int_list

def square_list_out_of_place(int_list):

    # we allocate a new list with the length of the input list
    squared_list = [None] * len(int_list)

    for index, element in enumerate(int_list):
        squared_list[index] = element ** 2

    return squared_list



