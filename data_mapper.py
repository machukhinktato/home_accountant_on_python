import sqlite3

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

    def find_by_id(self, name):
        statement = f"SELECT classification, name, value FROM category WHERE name=?"

        self.cursor.execute(statement, (name,))
        result = self.cursor.fetchall()
        if result:
            return Category(*result[0])
        else:
            raise RecordNotFoundException(f'record with id={name} not found')

    def insert(self, _category):
        statement = f"INSERT INTO category (classification, name, value) VALUES \
                              (?, ?, ?)"
        self.cursor.execute(statement, (_category.classification, _category.name, _category.value))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

        return f'insert successfully done'

    def update(self, _category):
        statement = f"UPDATE category SET value='{_category.value}' WHERE name='{_category.name}'"
        self.cursor.execute(statement)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, name):
        statement = f"DELETE FROM category WHERE name=?"
        self.cursor.execute(statement, ( name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class Category:
    def __init__(self, classification, name, value):
        self.classification = classification
        self.name = name
        self.value = value


financial_mapper = FinancialMapper(connection)
# category_1 = financial_mapper.find_by_id(1)
# print(category_1.__dict__)
#
# financial_mapper.insert(salary)
banana = financial_mapper.find_by_id('salary')
print(banana.__dict__)
financial_mapper.delete('salary')
print(banana.__dict__)