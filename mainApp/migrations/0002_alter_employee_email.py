# Generated by Django 4.2.3 on 2023-08-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]
