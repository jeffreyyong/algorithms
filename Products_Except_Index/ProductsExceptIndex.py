import unittest

def get_products(int_list):
    
    if len(int_list) < 2:
        raise IndexError('Needs at least two numbers')

    products_except_index = [None] * len(int_list)

    product_so_far = 1

    # for each integer, find the product of all the integers before it, storing the total product so far each time

    i = 0
    while i < len(int_list):
        products_except_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer, find the product of all the integers after it.
    # Since each index in products already ahs the products of all the integers 
    # before it, we're storing the total product of all other integers

    
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_except_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_except_index

class Test(unittest.TestCase):
    dataT = [[1, 7, 3, 4]]

    def test_products(self):
        # true check
        for test_string in self.dataT:
            actual = get_products(test_string)
            self.assertTrue(actual)


# python interpreter is running the source file as the main program, 
# it sets the special __name__ variable to have a value "__main""

# If the file is being imported from another module, __name__ will be set to the module's name

if __name__ == "__main__":
    unittest.main()

    







