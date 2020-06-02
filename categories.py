class Category:
    def __init__(self, title):
        self.title = title
        self.fin_stream = []

    def __str__(self):
        return f'{self.title}'

    def get_title(self):
        return f'{self.title}'

    def get_expense_sum(self):
        return sum(self.fin_stream)

    def get_expense_list(self):
        return self.fin_stream


