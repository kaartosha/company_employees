# База данных
import sqlite3


class DataBase:
    def __init__(self):
        self.__connection = sqlite3.connect('contacts.db')
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT,
                                 phone TEXT,
                                 email TEXT,
                                 salary TEXT)''')
        self.__connection.commit()

    # Добавление строки в БД
    def insert_data(self, name, phone, email, salary):
        self.__cursor.execute('''INSERT INTO users (name, phone, email, salary)
                                 VALUES (?, ?, ?, ?)''',
                              (name, phone, email, salary))
        self.__connection.commit()

    # Редактирование записи в БД
    def update_data(self, id, name, phone, email, salary):
        self.__cursor.execute('''UPDATE users
                                 SET name = ?, phone = ?, email = ?, salary = ?
                                 WHERE id = ?''',
                              (name, phone, email, salary, id))
        self.__connection.commit()

    # Удаление записи в БД
    def delete_data(self, id):
        self.__cursor.execute('''DELETE FROM users WHERE id = ?''',
                              (id, ))
        self.__connection.commit()

    # Поиск записи в БД
    def search_data(self, name):
        self.__cursor.execute('''SELECT * FROM users WHERE name LIKE ? ''',
                              ('%' + name + '%', ))
        return self.__cursor.fetchall()

    # Возвращает все данные БД
    def all_data(self):
        self.__cursor.execute('''SELECT * FROM users''')
        return self.__cursor.fetchall()

    # Возвращает одну строку данных
    def one_data(self, id):
        self.__cursor.execute('''SELECT * FROM users WHERE id = ?''', (id,))
        return self.__cursor.fetchone()
