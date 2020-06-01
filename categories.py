class Category:
    def __init__(self, title):
        self.title = title
        self.expenses = []

    def __str__(self):
        return f'{self.title}'

    def get_sum(self):
        return sum(self.expenses)

    def get_expense_list(self):
        return self.expenses



