# Generated by Django 3.2.9 on 2022-06-17 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20220617_0531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logger',
            old_name='checke',
            new_name='checked',
        ),
    ]
