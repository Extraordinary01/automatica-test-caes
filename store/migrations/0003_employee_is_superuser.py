# Generated by Django 3.2.7 on 2021-12-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_employee_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
