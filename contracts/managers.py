import pyodbc
from decimal import Decimal
class AccessManager:
    def __init__(self):
        self.connection = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\Nikolai\Desktop\depend_security_project\msaccess_project\departmental_security.accdb;'
        )
        self.cursor = self.connection.cursor()

# получаем клиента по имени
    def fetch_client_id_by_name(self, client_name):
        self.cursor.execute(
            "SELECT [id клиента] FROM [Клиент] WHERE [ФИО] = ?" , (client_name,)
        )
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

# получаем имена всех клиентов для меню
    def names_clients(self):
        self.cursor.execute('SELECT [ФИО] FROM [Клиент]')
        return [row[0] for row in self.cursor.fetchall()]

# получаем информацию по договору клиента
    def contract_client_information(self, contract_id):
        self.cursor.execute('''
        SELECT [Ежемесячная плата], [Срок начала действия], [Срок окончания действия] 
        FROM [Договор] 
        WHERE [id договора] = ?
        ''', (contract_id,))
        row = self.cursor.fetchone()
        return {
            'monthly_fee' : row[0],
            'effective_date' : row[1],
            'expiry_date' : row[2]
        }

# получаем все договора
    def fetch_all(self):
        self.cursor.execute('''SELECT 
    [Договор].[id договора] AS contract_id,
    [Договор].[Ежемесячная плата] AS monthly_fee,
    [Договор].[Срок начала действия] AS effective_date,
    [Договор].[Срок окончания действия] AS expiry_date,
    [Клиент].[ФИО] AS client_name,
    [Договор].[Скидка] AS sale
    FROM [Договор]
    LEFT JOIN [Клиент]
    ON [Договор].[id клиента] = [Клиент].[id клиента];''')
        return self.cursor.fetchall()

# создаем договор
    def create(self, monthly_fee, effective_date, expiry_date, client):
        monthly_fee = Decimal(monthly_fee)
        query = '''
            INSERT INTO [Договор] ([Ежемесячная плата], [Срок начала действия], [Срок окончания действия], [id клиента])
            VALUES (?, ?, ?, ?)
            '''
        self.cursor.execute(query, (monthly_fee, effective_date, expiry_date, client))
        self.connection.commit()

# обновляем договор
    def update(self, contract_id, monthly_fee, effective_date, expiry_date, client):
        monthly_fee = Decimal(monthly_fee)
        self.cursor.execute(
            '''UPDATE [Договор] SET [Ежемесячная плата] = ?, [Срок начала действия] = ?, [Срок окончания действия] = ?, [id клиента] = ?
            WHERE [id договора] = ?''',
            (monthly_fee, effective_date, expiry_date, client, contract_id)
        )
        self.connection.commit()

# удаляем договор
    def delete(self, contract_id):
        self.cursor.execute('DELETE FROM [Договор] WHERE [id договора] = ?', (contract_id,))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
