from categories import *


class BaseExpenses(BaseCategoriesMixin):
    expenses = []

    def __init__(self, title, expenses):
        self.title = title
        self.expenses.append(expenses)

    def __str__(self):
        return f'{self.title} {self.expenses}'


if __name__ == '__main__':
    c = BaseExpenses(Categories.title.get('products').title, 3000)
    c = BaseExpenses(Categories.title.get('products').title, 5000)
    print(c.title, sum(c.expenses))
