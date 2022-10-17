import sqlite3
from encryption.hash_login import hash_login


class UserInDataBase(Exception):
    pass


def is_acc_exist(login: str, password: str) -> tuple:
    """Проверка на присутствие таблицы в базе"""
    login_hash = hash_login(login, password)

    sqlite_connection = sqlite3.connect('security_data2.db')
    cursor = sqlite_connection.cursor()
    is_exist = f"""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{login_hash}';"""
    cursor.execute(is_exist)

    result = cursor.fetchone()[0]
    cursor.close()

    if sqlite_connection:
        sqlite_connection.close()

    if result:
        return True, login_hash

    return False, ''


def add_account(login: str, password: str) -> None:
    """Добавление аккаунта в базу"""
    if is_acc_exist(login, password)[0]:
        raise UserInDataBase()

    sqlite_connection = sqlite3.connect('security_data2.db')
    cursor = sqlite_connection.cursor()

    login_hash = hash_login(login, password)

    sqlite_create_table_query = f"""CREATE TABLE '{login_hash}' (name TEXT, data TEXT);"""

    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()

    cursor.close()

    if sqlite_connection:
        sqlite_connection.close()


def get_data(user_hash: str, storage_name: str, need_all=False) -> list:
    """Получение данных из таблицы"""

    sqlite_connection = sqlite3.connect('security_data2.db')
    cursor = sqlite_connection.cursor()
    if not need_all:
        query = f"""SELECT data FROM '{user_hash}'
                    WHERE name = '{storage_name}';"""
    else:
        query = f"""SELECT name FROM '{user_hash}';"""

    cursor.execute(query)

    result = cursor.fetchall()
    cursor.close()

    if sqlite_connection:
        sqlite_connection.close()

    return list(map(lambda x: x[0], result))


def set_data(storage_name: str, user_hash: str, data: str) -> None:
    """Добавление данных в хранилище"""
    sqlite_connection = sqlite3.connect('security_data2.db')
    cursor = sqlite_connection.cursor()
    query = f"""UPDATE '{user_hash}'
                SET data = '{data}'
                WHERE name = '{storage_name}';"""
    cursor.execute(query)
    sqlite_connection.commit()


def create_storage(storage_name: str, user_hash: str, data: str) -> None:
    """Создание хранилища"""
    sqlite_connection = sqlite3.connect('security_data2.db')
    cursor = sqlite_connection.cursor()
    query = f"""INSERT INTO '{user_hash}' (name, data) VALUES ('{storage_name}', '{data}');"""
    cursor.execute(query)
    sqlite_connection.commit()


def delete_storage(storage_name: str, user_hash: str):
    """Удаление хранилища"""
    sqlite_connection = sqlite3.connect('security_data2.db')
    cursor = sqlite_connection.cursor()
    query = f"""DELETE FROM '{user_hash}'
                WHERE name = '{storage_name}';"""
    cursor.execute(query)
    sqlite_connection.commit()

# print(get_data('282b43d6979667681a9f43c3792e5f8d6abb92658f916d5bb629229e3be6970e2ad8832120c5bcb5f9cf5434527e879d4f638af87901053306824cd1427b47c0', '1', True))