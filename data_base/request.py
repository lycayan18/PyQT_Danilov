import sqlite3
from encryption.hash_login import hash_login
import os


class UserInDataBase(Exception):
    pass

class InvalidData(Exception):
    pass


def connect_to_db(query: str, mode: str = 'r'):
    """Подключение к базе данных и проверка данных на валидность"""

    sqlite_connection = sqlite3.connect('security_data.db')
    sqlite_connection_copy = sqlite3.connect('security_data_copy.db')

    try:

        cursor = sqlite_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

    except sqlite3.DatabaseError:
        sqlite_connection.close()

        with open('security_data.db', 'w') as f:
            f.write('')

        sqlite_connection = sqlite3.connect('security_data.db')
        try:
            sqlite_connection_copy.backup(sqlite_connection)
            cursor = sqlite_connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except sqlite3.DatabaseError:
            with open('security_data_copy.db', 'w') as f:
                f.write('')
            sqlite_connection_copy.backup(sqlite_connection)
            return False

    if mode == 'w':
        sqlite_connection.commit()

    if mode == 'r':
        return result

    sqlite_connection.backup(sqlite_connection_copy)
    cursor.close()
    sqlite_connection.close()


def is_acc_exist(login: str, password: str) -> tuple:
    """Проверка на присутствие таблицы в базе"""

    login_hash = hash_login(login, password)
    query = f"""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{login_hash}';"""
    result = connect_to_db(query=query, mode='r')[0][0]

    if result:
        return True, login_hash

    return False, ''


def add_account(login: str, password: str) -> None:
    """Добавление аккаунта в базу"""

    if is_acc_exist(login, password)[0]:
        raise UserInDataBase()

    login_hash = hash_login(login, password)

    sqlite_create_table_query = f"""CREATE TABLE '{login_hash}' (name TEXT, data TEXT);"""
    connect_to_db(query=sqlite_create_table_query, mode='w')


def get_data(user_hash: str, storage_name: str, need_all=False) -> list:
    """Получение данных из таблицы"""

    if not need_all:
        query = f"""SELECT data FROM '{user_hash}'
                    WHERE name = '{storage_name}';"""
    else:
        query = f"""SELECT name FROM '{user_hash}';"""

    result = connect_to_db(query=query, mode='r')
    return list(map(lambda x: x[0], result))


def set_data(storage_name: str, user_hash: str, data: str) -> None:
    """Добавление данных в хранилище"""

    query = f"""UPDATE '{user_hash}'
                SET data = '{data}'
                WHERE name = '{storage_name}';"""
    connect_to_db(query=query, mode='w')


def create_storage(storage_name: str, user_hash: str, data: str) -> None:
    """Создание хранилища"""

    query = f"""INSERT INTO '{user_hash}' (name, data) VALUES ('{storage_name}', '{data}');"""
    connect_to_db(query=query, mode='w')


def delete_storage(storage_name: str, user_hash: str) -> None:
    """Удаление хранилища"""

    query = f"""DELETE FROM '{user_hash}'
                WHERE name = '{storage_name}';"""
    connect_to_db(query=query, mode='w')


def rename_table(old_name: str, new_name: str) -> None:
    """Преименование таблицы"""

    query = f"""ALTER TABLE '{old_name}' RENAME TO '{new_name}'"""
    connect_to_db(query=query, mode='w')


connect_to_db('', '')