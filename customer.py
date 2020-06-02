from categories import *


class Income:
    def __init__(self, category, value):
        self.category = category
        self.value = value
        self.category.expenses.append(self.value)
