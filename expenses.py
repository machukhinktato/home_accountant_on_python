from categories import *


class BaseExpenses(BaseCategoriesMixin):
    def __init__(self, title, expenses):
        self.title = title
        self.expenses = [expenses]

    def __str__(self):
        return f'{self.title} {self.expenses}'


if __name__ == '__main__':
    c = BaseExpenses(Categories.title.get('products').title, 3000)
    d = BaseExpenses(Categories.title.get('products').title, 5000)
    print(c.expenses[0])
    print(d.expenses[0])
    c = BaseExpenses(Categories.title.get('products').title, 7000)
    print(c.expenses[0])