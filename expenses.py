from categories import *


class BaseExpenses(BaseCategoriesMixin):
    # def __init__(self, name, expense):
    #     self.title = name
    #     self.expense = expense
    #
    # def __str__(self):
    #     return f'{self.title} {self.expense}'
    #
    # def __repr__(self):
    #     return f'{self.title} {self.expense}'
    pass




# print(type(Categories.title.keys()))
a = BaseExpenses(Products('Продукты', 0), 3000)
print(a)
