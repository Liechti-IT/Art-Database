# Generated by Django 4.2.3 on 2023-07-24 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='art_nr',
        ),
    ]
