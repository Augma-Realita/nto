import sqlite3

with open('markers_trained/8.zpt', 'rb') as f:
    image_blob = f.read()
    sqliteConnection = sqlite3.connect('db.sqlite')
    cursor = sqliteConnection.cursor()
    querry1 = """INSERT INTO markers (zpt_image) VALUES (?)"""
    data = [image_blob]
    cursor.execute(querry1, data)
    sqliteConnection.commit()
    cursor.close()


with open('markers_trained/9.zpt', 'rb') as f:
    image_blob = f.read()
    sqliteConnection = sqlite3.connect('db.sqlite')
    cursor = sqliteConnection.cursor()
    querry1 = """INSERT INTO markers (zpt_image) VALUES (?)"""
    data = [image_blob]
    cursor.execute(querry1, data)
    sqliteConnection.commit()
    cursor.close()

with open('markers_trained/10.zpt', 'rb') as f:
    image_blob = f.read()
    sqliteConnection = sqlite3.connect('db.sqlite')
    cursor = sqliteConnection.cursor()
    querry1 = """INSERT INTO markers (zpt_image) VALUES (?)"""
    data = [image_blob]
    cursor.execute(querry1, data)
    sqliteConnection.commit()
    cursor.close()


