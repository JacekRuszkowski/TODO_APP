# Generated by Django 3.1.7 on 2021-05-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_board_board_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=35),
        ),
    ]
