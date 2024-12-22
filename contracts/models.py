from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True, db_column = 'id клиента')
    full_name = models.CharField(max_length=255, db_column='ФИО')
    number = models.CharField(max_length=20, db_column='Номер телефона')
    mail =  models.EmailField(db_column='Почта')
    client_adress = models.CharField(max_length=100, db_column='Адрес')

    class Meta:
        db_table = '[Клиент]'

    def __str__(self):
        return self.full_name

class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True, db_column = 'id договора')
    monthly_fee = models.DecimalField(max_digits=8, decimal_places=2, db_column = 'Ежемесячная плата')
    effective_date = models.DateTimeField(db_column = 'Срок начала действия')
    expiry_date = models.DateTimeField(db_column = 'Срок окончания действия')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='Клиент')
    sale = models.DecimalField(max_digits=5, decimal_places=2, db_column = 'Скидка')

    class Meta:
        db_table = '[Договор]'
        ordering = ['contract_id']

