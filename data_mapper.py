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
            statement = f"SELECT name, classification, value FROM category WHERE name=?"

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

    def update(self, _category):
        statement = f"UPDATE category SET name=?, value=?, name=?"
        self.cursor.execute(statement, (_category.name, _category.value, _category.name))
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
