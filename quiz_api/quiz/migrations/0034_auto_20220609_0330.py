# Generated by Django 3.2.9 on 2022-06-09 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0033_auto_20220519_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentfield',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.parentquiz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parentfield',
            name='parent_status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.parentstatus'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='quiztaker',
            name='max_grade',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]