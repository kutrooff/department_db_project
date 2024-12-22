from symbol import namedexpr_test

import pyodbc
class AccessManager:
    def __init__(self):
        self.connection = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\Nikolai\Desktop\depend_security_project\msaccess_project\departmental_security.accdb;'
        )
        self.cursor = self.connection.cursor()

    def names_clients(self):
        self.cursor.execute('SELECT [ФИО] FROM [Клиент]')
        rows = self.cursor.fetchall()
        if rows:
            a = [row[0] for row in rows]
        else:
            a = "Пустой список"
        print(a)
