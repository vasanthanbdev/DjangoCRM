# Generated by Django 4.2.5 on 2023-09-15 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='addresss',
            new_name='address',
        ),
    ]
