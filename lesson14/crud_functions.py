import sqlite3

def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Products')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f"Product {i}", f"Description {i}", i * 100))
    cursor.execute('SELECT * FROM Products')
    res = cursor.fetchall()
    connection.commit()
    connection.close()
    return res
