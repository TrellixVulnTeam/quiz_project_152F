# Generated by Django 3.2.9 on 2022-02-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20211123_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
