from datetime import date

class Product(object):
    def __init__(self, name, price):
        # constructor to setup the Product
        # with given name and price
        self.name = name
        self.price = price
        self.discountRate = 0
        self.reductionDate = None

    def get_name(self):

        # return the name of the product
        return self.name

    def set_name(self, name):

        # Set the name of the product
        self.name = name

    def get_price(self):

        # return the price of the product
        return self.price

    def set_price(self, price):

        # set the price of the product
        self.price = price

    def get_discount_rate(self):

        # get the current discount rate
        return self.discountRate

    def set_discount_rate(self, discountRate):

        # set the discount rate of the product
        self.discountRate = discountRate

    def set_reduction_date(self, reductionDate):

        # set when the reduction is set on this product
        self.reductionDate = reductionDate

    def get_reduction_date(self):

        # get the reduction date
        return self.reductionDate

    def is_on_red_pencil(self, currentDate):

        # Function to check that the given product
        # is on Red_Pencil Promotion

        # First test, discount rate should be 5% to 30%
        if self.discountRate >= 0.05 and self.discountRate <= 0.3:

            # Check the reduction is within 30 days
            if self.reductionDate == None:
                return False
            else: # Check the days
                delta = currentDate - self.reductionDate
                if delta.days <= 30:
                    return True
                else:
                    return False
        else:
            return False
