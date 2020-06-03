class User:
    banana = {}

    def __init__(self, name):
        self.name = name
        self.category = {}
        self.balance = []
        self.account = {}

    def __str__(self):
        return f'{self.name}'

    def create_expense(self, name, value):
        self.banana.update({name: value})
        return self.banana


class Category:
    def __init__(self, name, balance, type_of='expense'):
        self.name = name
        self.__balance = balance
        self.main_category = type_of

    def __str__(self):
        return f'{self.__balance}'

    def __add__(self, other):
        pass

    def get_val(self):
        return f'{self.__balance}'

    def set_val(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('balance must have numeric symbols')
        self.__balance += value
        return self.__balance

    def del_val(self):
        del self.__balance


if __name__ == '__main__':
    user = User('Misha')
    new_expense = Category('products', 1000, 'income')
    print(new_expense.main_category)