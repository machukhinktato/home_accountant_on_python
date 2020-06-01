from categories import *


class Expenses:
    def __init__(self, category, value):
        self.category = category
        self.value = value
        self.category.expenses.append(self.value)


if __name__ == '__main__':
    products = Category('Продукты')
    car = Category('Машина')
    print(products)
    expense = Expenses(products, 1000)
    expense = Expenses(products, 1000)
    print(products.title, products.get_expense_list())
    print(car.title, car.get_sum())