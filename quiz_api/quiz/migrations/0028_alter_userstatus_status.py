# Generated by Django 3.2.9 on 2022-04-25 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0027_alter_userstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.parentstatus'),
        ),
    ]
