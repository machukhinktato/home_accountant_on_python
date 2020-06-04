class User:
    def __init__(self, name):
        self.name = name
        self.category = {}
        self.balance = []
        self.account = {}

    def __str__(self):
        return f'{self.name}'


def show_cat_val(category):
    if category.main_category == 'expense':
        print(category.main_category, category._balance)
        return
    return print(category.main_category, category._balance)

def show_user_streams(User):
    pass


class Category:
    def __init__(self, title, type_of='expense', balance=0):
        self.title = title
        self.main_category = type_of
        self._balance = balance

    def __str__(self):
        return f'{self.main_category} {self.title} {self._balance} '

    def __add__(self, other):
        pass

    def get_val(self):
        return f'{self.__balance}'

    def set_val(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('balance must have numeric symbols')
        self._balance += value
        return self._balance

    def annul_val(self):
        self._balance = 0


if __name__ == '__main__':
    user = User('Misha')
    products = Category('products')
    show_cat_val(products)
    print(user)