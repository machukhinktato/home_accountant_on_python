from user import *
from categories import *
from expenses import *


# (User, Category, FinancialStreams)
class Account:
    def __init__(self, customer):
        self.user = customer.name
        self.income = []

    def __str__(self):
        if self.income.__len__() > 0:
            return f'{self.user} {self.income[0]}'
        return self.user

    def set_income(self, income):
        self.income.append(income)

    # def __str__(self):
    #     return f'{self.user} {self.account} {self.expenses} {self.income}'
    #
    # def __repr__(self):
    #     return f'{self.user} {self.account} {self.expenses} {self.income}'
    #
    # def create_account(self, user):
    #     account_name = user
    #     self.user = account_name

    # def set_income(self, user):
    #     income_of_user = user
    #     self.income.append(income_of_user.income)
    #     return f'{self.income}'


if __name__ == '__main__':
    a = Account(User('Mike'))
    print(a.user, a.income)
    # a = User('Petya')
    # a.set_income(1000)
    # print(a)
    # a.create_account(User('Ivan'))
    # a.set_income(2000)
# if __name__ == '__main__':
#     products = Category('Products')
#     car = Category('Car')
#     print(products)
#     expense = Expenses(products, 1000)
#     expense = Expenses(products, 1000)
#     expense = Expenses(car, 5000)
#     expense = Expenses(products, 1000)
#     print(products.get_title(), products.get_expense_list(), products.get_expense_sum())
#     print(car.get_title(), car.get_expense_sum())
#     Builder(user__builder, 'Василий', 1000, 1500, 500)
#     user = user__builder.person
#     print(user.__dict__)
