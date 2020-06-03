class User:
    def __init__(self, name):
        self.name = name
        self.income_account = Bank.income_account
        self.expense_account = Bank.expense_account

    def __str__(self):
        return f'{self.name}'

    def set_expense(self, expense):
        self.expense_account.append(expense)
        return print('new expense with amount', self.expense_account[0], 'rub registered')

    def set_income(self, expense):
        self.income_account.append(expense)
        return self.income_account


class Bank:
    income_account = []
    expense_account = []


class Category:
    def __init__(self, title):
        self.title = title
        self.income_account = Bank.income_account
        self.expense_account = Bank.expense_account

    def __str__(self):
        return f'{self.title} {sum(self.income_account)} {sum(self.expense_account)} '


if __name__ == '__main__':
    user = User('Misha')
    print(user)
    user.set_income(2000)
    user.set_expense(1000)
    user.set_expense(3000)
    products = Category('products')
    print(products)