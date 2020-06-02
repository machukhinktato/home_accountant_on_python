from categories import *
from user import *


class FinancialStreams:
    def __init__(self, category, value):
        self.category = category
        self.value = value
        self.category.fin_stream.append(self.value)


if __name__ == '__main__':
    products = Category('Products')
    car = Category('Car')
    salary = Category('Income')
    print(products)
    expense = FinancialStreams(products, 1000)
    expense = FinancialStreams(products, 1000)
    expense = FinancialStreams(car, 5000)
    expense = FinancialStreams(products, 1000)
    income = FinancialStreams(salary, 1000)
    print(products.get_title(), products.get_expense_list(), products.get_expense_sum())
    print(car.get_title(), car.get_expense_sum())
    print(salary)
    print(salary.fin_stream)