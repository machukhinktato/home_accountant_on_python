class User:
    def __init__(self, name):
        self.name = name
        self.expense_account = Bank.expense_account
        self.income_account = Bank.income_account

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
    class Category:
        def __init__(self, title):
            self.title = title
            self.expense_account = Bank.expense_account
            self.income_account = Bank.income_account

        def __str__(self):
            return f'{self.title}'
    # def __init__(self):
    #     self.account = []
    #
    # def __str__(self):
    #     return self.account


if __name__ == '__main__':
    user = User('Misha')
    print(user)
    user.set_income(2000)
    user.set_expense(1000)

