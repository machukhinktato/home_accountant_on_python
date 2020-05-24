import abc
from user import *


class Accounts:
    accounts = []

    def __init__(self, account, income):
        self.accounts.append(account)
        self.income = income

    def __str__(self):
        return f'{self.accounts} income {self.income} rubles'

    def create_account(owner_name, income):
        user_account = Accounts(owner_name, income)
        return user_account


if __name__ == '__main__':
    Builder(user__builder, 'Василий', 1000, 1500, 500)
    Vasya = user__builder.person
    Builder(user__builder, 'Petya', 1000, 1500, 500)
    Petya = user__builder.person
    a = Accounts.create_account(Vasya.name, Vasya.income)
    b = Accounts.create_account(Petya.name, Petya.income)
    print(a)
    print(b)
