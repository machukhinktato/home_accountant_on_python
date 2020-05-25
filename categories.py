import abc


class AbstractCategory(metaclass=abc.ABCMeta):
    def __init__(self):
        self.category = Category_format()

    def post_income(self):
        pass

    def post_expense(self):
        pass


class Category_form:
    title = {}
    expense = 0
    income = 0
