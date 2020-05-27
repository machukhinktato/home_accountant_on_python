from categories import Categories


class BaseExpenses:
    def __init__(self, name, expense):
        self.title = name
        self.expense = expense

    #
    def __str__(self):
        return f'{self.title} {self.expense}'

    # def __repr__(self):
    #     return f'{self.title} {self.expense}'
    # pass


# b = Categories.title.get('products')
# a = BaseExpenses(b.title, 3000)
c = BaseExpenses(Categories.title.get('products').title, 3000)

# print(a)
print(c)
