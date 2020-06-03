class Category:
    def __init__(self, title):
        self.title = title
        self.fin_stream = []
        self.income = []

    def __str__(self):
        return f'{self.title}'

    def create_category(self, title):
        self.title = title

    def get_title(self):
        return f'{self.title}'

    def set_title(self, title):
        self.title = title
        return title

    def get_expense_sum(self):
        return sum(self.fin_stream)

    def get_expense_list(self):
        return self.fin_stream


def create_category(self, title):
    self.title = title


if __name__ == '__main__':
    a = Category
    a.create_category('products')
