# Generated by Django 4.1.7 on 2023-03-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('second_name', models.CharField(max_length=250)),
                ('amount_paid', models.IntegerField()),
                ('date_of_payment', models.CharField(max_length=250)),
                ('date_due_payment', models.CharField(max_length=250)),
            ],
        ),
    ]
