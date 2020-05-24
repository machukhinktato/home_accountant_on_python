import abc
from user import User


class Account:
    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.expenses = []

    def __str__(self):
        return f'пользователь {self.name} доходы {self.income}'

    def create_account(owner_name, income):
        user_account = Account(owner_name, income)
        return user_account

    def add_expense(user_account):
        expense =


if __name__ == '__main__':
    a = Account.create_account('Vasya', 1000)
    print(a)
