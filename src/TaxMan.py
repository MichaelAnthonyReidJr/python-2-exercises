class TaxMan:

    def __init__(self, items, sales_tax_string):
        self.items = items 
        self.sales_tax = float(sales_tax_string.strip('%')) / 100
        #print(self.sales_tax)
        self.__total_sum = 0

    def calc_total(self):
        total_price = 0
        for eachItem in self.items:
            total_price += eachItem['price']
        self.__total_sum += round(total_price * (1 + self.sales_tax),2)
       
    def get_total(self):
        return self.__total_sum
    





