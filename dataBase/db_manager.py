import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()


connection.commit()
connection.close()
