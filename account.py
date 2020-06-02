from user import *
from categories import *
from expenses import *


class Account:
    def __init__(self, user, expenses):
        self.user = user
        self.expenses = expenses


if __name__ == '__main__':
    products = Category('Products')
    car = Category('Car')
    print(products)
    expense = Expenses(products, 1000)
    expense = Expenses(products, 1000)
    expense = Expenses(car, 5000)
    expense = Expenses(products, 1000)
    print(products.get_title(), products.get_expense_list(), products.get_expense_sum())
    print(car.get_title(), car.get_expense_sum())
    Builder(user__builder, 'Василий', 1000, 1500, 500)
    user = user__builder.person
    print(user.__dict__)