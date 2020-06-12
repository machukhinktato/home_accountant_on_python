import sqlite3
import threading

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

        self.cursor.execute(statement, (_category.name,))
        result = self.cursor.fetchall()
        if result:
            return Category(*result[0])
        else:
            raise RecordNotFoundException(f'record with name={_category.name} not found')

    # def call_all(self):
    #     statement = f"-- SELECT * FROM category WHERE name IS NOT NULL "
    #     self.cursor.execute(statement)
    #     result = self.cursor.fetchall()
    #     return result
        # if result:
        #     return Category(*result)

    # def search_by_name(self, _category):
    #     statement = f"SELECT classification, name, value FROM category WHERE name=?"
    #
    #     self.cursor.execute(statement, (_category.name,))
    #     result = self.cursor.fetchall()
    #     if result:
    #         return Category(*result[0])
    #     else:
    #         raise RecordNotFoundException(f'record with name={_category.name} not found')
    #

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


# class MapperRegistry:
#     @staticmethod
#     def get_mapper(obj):
#         if isinstance(obj, Category):
#             return FinancialMapper(connection)
#
#
# class UnitOfWork:
#     current = threading.local()
#
#     def __init__(self):
#         self.new_objects = []
#         self.dirty_objects = []
#         self.removed_objects = []
#
#     def register_new(self, obj):
#         self.new_objects.append(obj)
#
#     def register_dirty(self, obj):
#         self.dirty_objects.append(obj)
#
#     def register_removed(self, obj):
#         self.removed_objects.append(obj)
#
#     def commit(self):
#         self.insert_new()
#         self.update_dirty()
#         self.delete_removed()
#
#     def insert_new(self):
#         for obj in self.new_objects:
#             MapperRegistry.get_mapper(obj).insert(obj)
#
#     def update_dirty(self):
#         for obj in self.dirty_objects:
#             MapperRegistry.get_mapper(obj).update(obj)
#
#     def delete_removed(self):
#         for obj in self.removed_objects:
#             MapperRegistry.get_mapper(obj).delete(obj)
#
#     @staticmethod
#     def new_current():
#         __class__.set_current(UnitOfWork())
#
#     @classmethod
#     def set_current(cls, unit_of_work):
#         cls.current.unit_of_work = unit_of_work
#
#     @classmethod
#     def get_current(cls):
#         return cls.current.unit_of_work
#
#
# class DomainObject:
#
#     def mark_new(self):
#         UnitOfWork.get_current().register_new(self)
#
#     def mark_dirty(self):
#         UnitOfWork.get_current().register_dirty(self)
#
#     def mark_removed(self):
#         UnitOfWork.get_current().register_removed(self)



class Category:
    def __init__(self, classification, name, value):
        self.classification = classification
        self.name = name
        self.value = value


financial_mapper = FinancialMapper(connection)
# result = financial_mapper.call_all()
# print(result)
# if result.name == dontated:
#     result.name.delete()
# result = financial_mapper.call_all()
# try:
#     UnitOfWork.new_current()
#     new_person_1 = Category('expense', 'donated', 1000)
#     new_person_2 = Category('income', 'salary', 1000)
#     new_person_1.mark_new()
#     new_person_2.mark_new()
#
#     category_mapper = FinancialMapper(connection)
#     exists_category_1 = category_mapper.search(new_person_1)
#     exists_category_1.mark_dirty()
#     print(exists_category_1.__dict__)
#     exists_category_1.name += ' on 10 day of march'
#     print(exists_category_1.name)
#
#     exists_cat_2 = category_mapper.search(new_person_2)
#     print(exists_cat_2.__dict__)
#     exists_cat_2.value += 1500
#     exists_cat_2.mark_dirty()
#
#     print(UnitOfWork.get_current().__dict__)
#
#     UnitOfWork.get_current().commit()
# except Exception as e:
#     print(e.args)
# finally:
#     UnitOfWork.set_current(None)
#
# print(UnitOfWork.get_current())
