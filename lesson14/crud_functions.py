import sqlite3


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL DEFAULT 1000
    );
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    return products

def add_user(username, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    if not is_include(username):
        cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)",
                       (f'{username}', f'{email}', f'{age}'))
    connection.commit()
    connection.close()

def is_include(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        flag = False
    else:
        flag = True
    connection.commit()
    connection.close()
    return flag

