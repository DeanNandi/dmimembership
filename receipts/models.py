from django.db import models

class Patients(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    amount_paid = models.IntegerField()
    date_of_payment = models.CharField(max_length=250)
    date_due_payment = models.CharField(max_length=250)

