import sqlite3
from test import FinancialMapper, DomainObject


class User:
    def __init__(self, name):
        self.name = name
        self.category = []

    def __str__(self):
        return f'{self.name} {self.category[:]}'

    def bind_category(self, category):
        self.category.append(category)

    def categories(self, name=None):
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


class FinancialOperator(DomainObject):
    def __init__(self, name, classification='expense', balance=0):
        self.name = name.lower()
        self.classification = classification
        self.value = balance

    def __str__(self):
        return f'{self.name} {self.classification} {self.value} '

    def __repr__(self):
        return f'{self.name} {self.classification} {self.value} '

    def __add__(self, other):
        pass

    # next three methods are out of use
    # decision about their future will be made later

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
        try:
            financial_mapper.insert(self)
        except Exception as e:
            print(e.args)

    def update_db_data(self, value):
        _category = financial_mapper.search(self)
        _category.value += value
        financial_mapper.update(self, _category.value)

    def delete_from_db(self):
        _category = financial_mapper.search(self)
        financial_mapper.delete(self)

    def search(self):
        result = financial_mapper.search(self)
        return result.__dict__

    def call_all(self):
        result = financial_mapper.call_all()
        return result


# if __name__ == '__main__':
    # user = User('Misha')
    # salary = FinancialOperator('salary', 'income')
    # salary1 = FinancialOperator('salary', 'income')
    # user.bind_category(salary)
    # user.bind_category(salary1)
    # user.categories(salary).insert_into_db()
    # user.categories(salary1).insert_into_db()
    # searcher = financial_mapper.search_by_name('products')
    # print(searcher.__dict__)
    # user.categories(salary).update_db_data(1500)
    # print(user.categories(salary))
    # user.categories(salary).update_db_data(1550)
    # print(user.categories(salary))
    # user.categories(salary).delete_from_db()
    # print(user.categories(salary))