import sqlite3
from app.encryption.hash_login import hash_login


class UserInDataBase(Exception):
    pass


def is_acc_exist(login: str, password: str) -> tuple:
    """Проверка на присутствие таблицы в базе"""

    login_hash = hash_login(login, password)

    sqlite_connection = sqlite3.connect('security_data.db')
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

    sqlite_connection = sqlite3.connect('security_data.db')
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

    sqlite_connection = sqlite3.connect('security_data.db')
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

    sqlite_connection = sqlite3.connect('security_data.db')
    cursor = sqlite_connection.cursor()
    query = f"""UPDATE '{user_hash}'
                SET data = '{data}'
                WHERE name = '{storage_name}';"""
    cursor.execute(query)
    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()


def create_storage(storage_name: str, user_hash: str, data: str) -> None:
    """Создание хранилища"""

    sqlite_connection = sqlite3.connect('security_data.db')
    cursor = sqlite_connection.cursor()
    query = f"""INSERT INTO '{user_hash}' (name, data) VALUES ('{storage_name}', '{data}');"""
    cursor.execute(query)
    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()


def delete_storage(storage_name: str, user_hash: str) -> None:
    """Удаление хранилища"""

    sqlite_connection = sqlite3.connect('security_data.db')
    cursor = sqlite_connection.cursor()
    query = f"""DELETE FROM '{user_hash}'
                WHERE name = '{storage_name}';"""
    cursor.execute(query)
    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()


def rename_table(old_name: str, new_name: str) -> None:
    """Преименование таблицы"""
    sqlite_connection = sqlite3.connect('security_data.db')
    cursor = sqlite_connection.cursor()
    query = f"""ALTER TABLE '{old_name}' RENAME TO '{new_name}'"""
    cursor.execute(query)
    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()

