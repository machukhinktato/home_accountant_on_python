from categories import *


class BaseExpenses(BaseCategoriesMixin):
    def __init__(self, name, expense):
        self.title = name
        self.expense = expense

    def __str__(self):
        return f'{self.title} {self.expense}'


print(type(Categories.title.keys()))
a = BaseExpenses(Categories.title['products'], 5000)
print(a)
