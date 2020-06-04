class BudgetKeeper:
    def __init__(self, title, balance, type_of='expense'):
        self.title = title
        self.__balance = balance
        self.main_category = type_of

    def __str__(self):
        return f'{self.title} {self.__balance} {self.main_category}'

    def __add__(self, other):
        pass

    def get_val(self):
        return f'{self.__balance}'

    def set_val(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('balance must have numeric symbols')
        self.__balance += value
        return self.__balance

    def annul_val(self):
        self.__balance = 0


if __name__ == '__main__':
    user = User('Misha')
