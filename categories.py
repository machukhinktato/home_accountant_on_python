import abc


class AbstractCategory(metaclass=abc.ABCMeta):
    def __init__(self):
        self.category = Category()

    def set_income(self):
        pass

    def get_expense(self):
        pass


