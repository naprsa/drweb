# Generated by Django 3.1.5 on 2021-01-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210124_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookonshelf',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Позиция на полке'),
        ),
    ]
