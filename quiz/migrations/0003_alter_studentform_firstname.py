# Generated by Django 4.1.2 on 2022-10-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_studentform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentform',
            name='firstname',
            field=models.CharField(max_length=50, verbose_name='Enter unit name'),
        ),
    ]
