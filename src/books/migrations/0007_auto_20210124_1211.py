# Generated by Django 3.1.5 on 2021-01-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210124_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookonshelf',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='Позиция на полке'),
        ),
    ]