# Generated by Django 3.1.5 on 2021-01-23 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210123_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookonshelf',
            options={'ordering': ['position']},
        ),
    ]
