class User:
    def __init__(self, name, category=None):
        self.name = name
        self.category = [category]

    def __str__(self):
        return f'{self.name} {self.category[:]}'

    def bind_category(self, category):
        if not category in self.category:
            self.category.append(category)
        else:
            print('category already exists')
        if None in self.category:
            self.category.pop(0)

    def show_balance(self):
        income = show_income_sum(self)
        expense = show_expense_sum(self)
        res = income - expense
        print(res)
        return res

    def show_financial_streams(self):
        for val in self.category[:]:
            print(val)
        return val


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
        return f'{self._balance}'

    def set_val(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('balance must have numeric symbols')
        self._balance += value
        return self._balance

    def annul_val(self):
        self._balance = 0


def show_income_sum(user):
    income_list = user.category[:]
    sum_list = []
    for value in income_list:
        if value.main_category == 'income':
            sum_list.append(value._balance)
    return sum(sum_list)


def show_expense_sum(user):
    expense_list = user.category[:]
    sum_list = []
    for value in expense_list:
        if value.main_category == 'expense':
            sum_list.append(value._balance)
    return sum(sum_list)


def show_financial_streams(user):
    for val in user.category[:]:
        print(val)
    return val


if __name__ == '__main__':
    user = User('Misha')
    salary = Category('salary', 'income')
    robbery = Category('robbery', 'income')
    products = Category('products')
    user.bind_category(salary)
    user.category[0].set_val(10000)
    user.bind_category(products)
    user.category[1].set_val(5000)
    user.category[1].set_val(15000)
    user.bind_category(robbery)
    user.category[2].set_val(5000)
    user.show_financial_streams()
    # print(type(False))
