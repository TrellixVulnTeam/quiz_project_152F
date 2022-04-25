# Generated by Django 3.2.9 on 2022-04-25 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0029_alter_userstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='quiz_taker',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_status', to='quiz.quiztaker'),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='status',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.parentstatus'),
        ),
    ]
