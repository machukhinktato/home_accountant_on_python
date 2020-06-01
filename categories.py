class Category:
    def __init__(self, name, expenses):
        self.name = name
        self.expenses = expenses

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'


class Expenses:
    def __init__(self, category, value):
