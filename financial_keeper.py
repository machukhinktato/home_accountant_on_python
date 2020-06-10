from data_mapper import *


class User:
    def __init__(self, name):
        self.name = name
        self.category = []

    def __str__(self):
        return f'{self.name} {self.category[:]}'

    def bind_category(self, category):
        self.category.append(category)

    def categories(self, name):
        categories = []
        for i in self.category:
            if name in self.category[:]:
                categories.append(i)
                return categories[0]

    def show_sum(self, classification):
        sum_list = self.category[:]
        calculator = []
        for value in sum_list:
            if value.classification == classification:
                calculator.append(value.value)
                res = int(sum(calculator))
        return res

    def show_income_sum(self):
        income = self.show_sum('income')
        return f'income {income}'

    def show_expense_sum(self):
        expense = self.show_sum('expense')
        return f'expense {expense}'

    def show_balance(self):
        ttl_income = self.show_sum('income')
        ttl_expense = self.show_sum('expense')
        ttl = ttl_income - ttl_expense
        return f'{ttl}'


    def show_financial_streams(self):
        for val in self.category[:]:
            print(val.title, val.value)


class Category:
    def __init__(self, name, classification='expense', balance=0):
        self.name = name.lower()
        self.classification = classification
        self.value = balance

    def __str__(self):
        return f'{self.classification} {self.name} {self.value} '

    def __repr__(self):
        return f'{self.classification} {self.name} {self.value} '

    def __add__(self, other):
        pass

    def get_val(self):
        return print(self.name, self.value)

    def set_val(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('balance must have numeric symbols')
        self.value += value
        return self.value

    def annul_val(self):
        self.value = 0
        return print(self.name, self.value)

    def insert_into_db(self):
        # financial_mapper = FinancialMapper(connection)
        financial_mapper.insert(self)


if __name__ == '__main__':
    user = User('Misha')
    salary = Category('salary', 'income')
    robbery = Category('robbery', 'income')
    products = Category('products')
    donated = Category('donated')
    print(donated)
    donated.insert_into_db()
    user.bind_category(salary)

    # user.categories(salary).set_val(10000)
    # print(user.categories(salary).get_val())
    # user.category[0].set_val(10000)
    # user.bind_category(products)
    # user.category[1].set_val(5000)
    # user.category[1].set_val(15000)
    # user.bind_category(robbery)
    # user.bind_category(donated)
    # user.category[2].set_val(5000)
    # user.category[3].set_val(10)
    # user.show_financial_streams()
    # print('_' * 30)
    # print(user.show_income_sum())
    # print('_' * 30)
    # print(user.show_expense_sum())
    # print('_' * 30)
    # print(user.show_balance())
    # print('_' * 30)
    # user.category[1].set_val(1000)
    # user.show_financial_streams()
    # print('_' * 30)
    # user.category[2].get_val()
    # user.category[2].annul_val()
    # user.category[2].set_val(3000)
    # user.category[2].get_val()
    # print(user.category[:])
    # products = Category('products')
