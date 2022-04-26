# Generated by Django 3.2.9 on 2022-04-23 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_grade_level'),
        ('quiz', '0022_question_taken_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiztaker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AlterField(
            model_name='quiztaker',
            name='user_status',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_taker', to='quiz.userstatus'),
        ),
    ]