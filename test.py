import sqlite3
import threading
# from financial_keeper import FinancialOperator

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
            return Category(*result[0])
        else:
            raise RecordNotFoundException(f'record with name={_category.name} not found')

    def search_by_name(self, name):
        try:
            statement = f"SELECT classification, name, value FROM category WHERE name=?"

            self.cursor.execute(statement, (name,))
            result = self.cursor.fetchall()
            if result:
                return Category(*result[0])
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

    def update(self, _category, value):
        _category.value = value
        statement = f"UPDATE category SET value=? WHERE name=?"
        self.cursor.execute(statement, (_category.value, _category.name))
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


class MapperRegistry:
    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, FinancialOperator):
            return FinancialMapper(connection)


class UnitOfWork:
    """
    Паттерн UNIT OF WORK
    """
    # Работает с конкретным потоком
    current = threading.local()

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


class DomainObject:

    def mark_new(self):
        UnitOfWork.get_current().register_new(self)

    def mark_dirty(self):
        UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        UnitOfWork.get_current().register_removed(self)


class Person(DomainObject):
    def __init__(self, id_person, first_name, last_name):
        self.id_person = id_person
        self.last_name = last_name
        self.first_name = first_name


class Category(DomainObject):
    def __init__(self, name):
        self.name = name


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


class CategoryMapper:
    pass


try:
    UnitOfWork.new_current()
    new_person_1 = FinancialOperator('expense', 'car', 1000)
    new_person_1.mark_new()

    new_person_2 = FinancialOperator('expense', 'air', 13000)
    new_person_2.mark_new()

    financial_mapper = FinancialMapper(connection)
    exists_person_1 = financial_mapper.search_by_name('car')
    print(exists_person_1)
    exists_person_1.mark_dirty()
    print(exists_person_1.name)
    exists_person_1.name += ' Senior'
    print(exists_person_1.name)

    exists_person_2 = financial_mapper.search_by_name('air')
    exists_person_2.mark_removed()

    print(UnitOfWork.get_current().__dict__)

    UnitOfWork.get_current().commit()
# except Exception as e:
#     print(e.args)
finally:
    UnitOfWork.set_current(None)

print(UnitOfWork.get_current())
