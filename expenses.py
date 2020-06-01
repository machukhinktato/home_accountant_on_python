from categories import *


class Expenses:
    def __init__(self, category, value):
        self.category = category
        self.value = value
        self.category.expenses.append(self.value)


if __name__ == '__main__':
    products = Category('Products')
    car = Category('Car')
    print(products)
    expense = Expenses(products, 1000)
    expense = Expenses(products, 1000)
    expense = Expenses(car, 5000)
    expense = Expenses(products, 1000)
    print(products.get_title(), products.get_expense_list(), products.get_sum())
    print(car.get_title(), car.get_sum())
