# Generated by Django 3.0.5 on 2020-05-30 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Moive',
            new_name='Movie',
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-year', 'title')},
        ),
    ]
