import sqlite3
import threading
# from data_mapper import FinancialMapper


connection = sqlite3.connect('fin_keeper.db')


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class FinancialMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def search(self, _category):
        statement = f"SELECT classification, name, value FROM category WHERE name=?"

        self.cursor.execute(statement, (_category.name))
        result = self.cursor.fetchall()
        if result:
            return FinancialOperations(*result[0])
        else:
            raise RecordNotFoundException(f'record with name={_category.name} not found')

    def search_by_name(self, name):
        try:
            statement = f"SELECT name, classification, value FROM category WHERE name=?"

            self.cursor.execute(statement, (name,))
            result = self.cursor.fetchall()
            if result:
                return FinancialOperations(*result[0])
            else:
                raise RecordNotFoundException(f'record with name={name} not found')
        except Exception as e:
            print(e.args)

    def insert(self, _category):
        statement = f"INSERT INTO category (classification, name, value) VALUES \
                              (?, ?, ?)"
        self.cursor.execute(statement, (_category.classification, _category.name, _category.value))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, _category):
        statement = f"UPDATE category SET name=?, value=?, name=?"
        self.cursor.execute(statement, (_category.name.lower(), _category.value, _category.name.lower()))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, _category):
        statement = f"DELETE FROM category WHERE name=?"
        self.cursor.execute(statement, (_category.name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


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


class MapperRegistry:
    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, FinancialOperations):
            return FinancialMapper(connection)


class UnitOfWork:
    current = threading.local()
    financial_registry = {}

    def __init__(self):
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []

    def register_new(self, obj):
        self.new_objects.append(obj)

    def register_dirty(self, obj):
        self.dirty_objects.append(obj)

    def register_removed(self, obj):
        self.removed_objects.append(obj)

    def commit(self):
        self.insert_new()
        self.update_dirty()
        self.delete_removed()

    def insert_new(self):
        for obj in self.new_objects:
            MapperRegistry.get_mapper(obj).insert(obj)

    def update_dirty(self):
        for obj in self.dirty_objects:
            MapperRegistry.get_mapper(obj).update(obj)

    def delete_removed(self):
        for obj in self.removed_objects:
            MapperRegistry.get_mapper(obj).delete(obj)

    @staticmethod
    def new_current():
        __class__.set_current(UnitOfWork())

    @classmethod
    def set_current(cls, unit_of_work):
        cls.current.unit_of_work = unit_of_work

    @classmethod
    def get_current(cls):
        return cls.current.unit_of_work

    # @classmethod
    # def add_fin_ops(cls, financial_operation):
    #     if financial_operation.name not in cls.financial_registry.keys():
    #         cls.financial_registry[financial_operation.name] = financial_operation

    # @classmethod
    # def get_fin_ops(cls, key):
    #     if key in cls.financial_registry.keys():
    #         return cls.financial_registry[key]
    #     else:
    #         return None


class DomainObject:

    def mark_new(self):
        UnitOfWork.get_current().register_new(self)
        # UnitOfWork.get_current().add_fin_ops(self)

    def mark_dirty(self):
        UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        UnitOfWork.get_current().register_removed(self)


class FinancialOperations(DomainObject):
    def __init__(self, name, classification='expense', balance=0):
        self.name = name.lower()
        self.classification = classification
        self.value = balance

    def __str__(self):
        return f'{self.name} {self.value} {self.classification}'

    def __repr__(self):
        return f'{self.name} {self.value} {self.classification}'


try:
    UnitOfWork.new_current()
    financial_mapper = FinancialMapper(connection)
    car = FinancialOperations('car', 'expense', 1000)
    car.mark_new()
    result = financial_mapper.search_by_name('car')
    print(result)
    # UnitOfWork.get_current().add_fin_ops(car)
    # print(UnitOfWork.financial_registry)
    # print(new_person_1.__class__)
    #
    # new_person_2 = Category('air', 'expense', 13000)
    # print(new_person_2)
    # new_person_2.mark_new()
    #

    # exists_person_1 = financial_mapper.search_by_name('car uniqlo TATARY')
    # print(exists_person_1.__dict__)
    # print(exists_person_1.__class__)
    # exists_person_1.name += ' nouseSSSSS'
    # print(exists_person_1.__dict__)
    # print(exists_person_1.__class__)
    # exists_person_1.mark_dirty()
    # print(exists_person_1.name)
    # exists_person_2 = financial_mapper.search_by_name('car')
    # print(exists_person_2.__dict__)
    # exists_person_1.mark_removed()
    # exists_person_3 = financial_mapper.search_by_name('air')
    # exists_person_3.mark_removed()
    UnitOfWork.get_current().commit()
# except Exception as e:
#     print(e.args)
finally:
    UnitOfWork.set_current(None)
