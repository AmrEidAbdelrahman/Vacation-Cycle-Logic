# Generated by Django 4.0.1 on 2022-01-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_employee_hiring_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialvacation',
            name='date',
            field=models.DateField(),
        ),
    ]