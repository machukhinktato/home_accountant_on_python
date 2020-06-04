class User:
    def __init__(self, name, category=None):
        self.name = name
        self.category = [category]
        self.balance = []
        self.account = {}

    def __str__(self):
        return f'{self.name} {self.category[1:]}'

    def bind_category(self, category):
        if not category in self.category:
            self.category.append(category)
        else:
            print('category already exists')


# def show_cat_val(category):
#     if category.main_category in category.main_category:
#         for expense in category.main_category:
#             return print(expense)
#     return print(category.main_category, category._balance)
#
#
# def show_user_streams(User):
#     pass


class Category:
    def __init__(self, title, type_of='expense', balance=0):
        self.title = title.lower()
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
    salary = Category('salary', 'income')
    robbed = Category('robbed', 'income')
    products = Category('products')
    user.bind_category(salary)
    user.category[1].set_val(10000)
    user.bind_category(products)
    user.category[2].set_val(5000)
    user.bind_category(robbed)
    user.category[3].set_val(5000)
    print(user.category[2])
    show_cat_val(user.category)