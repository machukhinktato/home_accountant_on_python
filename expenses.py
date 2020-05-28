from categories import *


class BaseExpenses(BaseCategoriesMixin):
    def __init__(self, title, expenses):
        self.title = title
        self.expenses = [expenses]

    #
    def __str__(self):
        return f'{self.title} {self.expenses}'

    # def __repr__(self):
    #     return f'{self.title} {self.expense}'
    # pass


# b = Categories.title.get('products')
# a = BaseExpenses(b.title, 3000)
c = BaseExpenses(Categories.title.get('products').title, 3000)
d = BaseExpenses(Categories.title.get('products').title, 5000)
# print(a)
print(c)
print(d)
print(c.expenses.count())
