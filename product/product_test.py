import unittest

from product import Product
from datetime import date

class TestProduct(unittest.TestCase):

    def test_constructor(self):
        print("Testing Constructor of Product Class")
        prod = Product("Phone", 25)
        expected = "Phone"
        actual = prod.get_name()
        self.assertEqual(expected, actual)

    def test_get_name(self):
        print("Testing get_name() Product Class")
        prod = Product("Phone", 25)
        expected = "Phone"
        actual = prod.get_name()
        self.assertEqual(expected, actual)

    def test_set_name(self):
        print("Testing set_name() of Product Class")
        prod = Product("Phone", 25)
        prod.set_name("Television")
        expected = "Television"
        actual = prod.get_name()
        self.assertEqual(expected, actual)

    def test_get_price(self):
        print("Testing get_price of Product Class")
        prod = Product("Phone", 25)
        expected = 25
        actual = prod.get_price()
        self.assertEqual(expected, actual)

    def test_set_price(self):
        print("Testing set_price of Product Class")
        prod = Product("Phone", 25)
        prod.set_price(30)
        expected = 30
        actual = prod.get_price()
        self.assertEqual(expected, actual)

    def test_set_reduction_rate(self):
        print("Testing set_discount_rate of Product Class")
        prod = Product("Phone", 25)
        prod.set_discount_rate(0.07)
        expected = 0.07
        actual = prod.get_discount_rate()
        self.assertEqual(expected, actual)

    def test_set_reduction_rate(self):
        print("Testing get_discount_rate of Product Class")
        prod = Product("Phone", 25)
        prod.set_discount_rate(0.07)
        expected = 0.07
        actual = prod.get_discount_rate()
        self.assertEqual(expected, actual)

    def test_set_reduction_date(self):
        print("Testing set_reduction_date of Product Class")
        prod = Product("Phone", 25)
        prod.set_discount_rate(0.07)
        prod.set_reduction_date(date(2017, 9, 21))
        expected = date(2017, 9, 21)
        actual = prod.get_reduction_date()
        self.assertEqual(expected, actual)

    def test_get_reduction_date(self):
        print("Testing get_reduction_date of Product Class")
        prod = Product("Phone", 25)
        prod.set_discount_rate(0.07)
        prod.set_reduction_date(date(2017, 9, 21))
        expected = date(2017, 9, 21)
        actual = prod.get_reduction_date()
        self.assertEqual(expected, actual)

    # For red pencil promotion
    def test_red_pencil_test1(self):
        print("Testing red_pencil_test_1 of Product Class")
        prod = Product("Phone", 25)
        prod.set_discount_rate(0.07)
        prod.set_reduction_date(date(2017, 8, 21))
        expected = True
        actual = prod.is_on_red_pencil(date(2017, 9, 10))
        self.assertEqual(expected, actual)

    def test_red_pencil_test2(self):
        print("Testing red_pencil_test_2 of Product Class")
        prod = Product("Phone", 25)

        prod.set_discount_rate(0.07)
        prod.set_reduction_date(date(2017, 8, 21))
        expected = True
        actual = prod.is_on_red_pencil(date(2017, 9, 10))
        self.assertEqual(expected, actual)

        prod.set_discount_rate(0.35)
        expected = False
        actual = prod.is_on_red_pencil(date(2017, 9, 10))
        self.assertEqual(expected, actual)


    def test_red_pencil_test3(self):
        prod = Product("Phone", 25)

        prod.set_discount_rate(0.07)

        prod.set_reduction_date(date(2017, 7, 21))
        expected = False

        actual = prod.is_on_red_pencil(date(2017, 9, 21))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    if __name__ == '__main__':
        print("\n\n\n\n\n\n\n\n")
        unittest.main()


