class Category:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'


class Expenses:
    def __init__(self, category, value):
        self.category = category
        self.value = value
        self.category.expenses.append(self.value)

