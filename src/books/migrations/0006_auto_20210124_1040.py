# Generated by Django 3.1.5 on 2021-01-24 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210123_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookonshelf',
            name='position',
            field=models.PositiveIntegerField(unique=True, verbose_name='Позиция на полке'),
        ),
        migrations.AlterField(
            model_name='bookonshelf',
            name='shelf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_on_shelf', to='books.shelf'),
        ),
    ]