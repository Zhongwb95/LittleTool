
import sqlite3


class DBConn(object):
    sql_create_table = 'CREATE TABLE company ' \
                       '(id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL,' \
                       ' age INT NOT NULL, address CHAR(50), salary REAL);'
    sql_insert_data = ''

    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        self.create_table()

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_table(self):
        self.cursor.execute(self.sql_create_table)
        self.conn.commit()

    def insert(self, args):
        self.cursor.execute(self.sql_insert_data, args)
        pass
