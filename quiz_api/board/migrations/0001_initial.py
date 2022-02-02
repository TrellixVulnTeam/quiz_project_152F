# Generated by Django 3.2.9 on 2022-02-01 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=70)),
                ('slug', models.SlugField(blank=True)),
                ('solved', models.BooleanField(default=False)),
                ('good', models.IntegerField(default=0)),
                ('tag', models.CharField(blank=True, max_length=20)),
                ('vote', models.IntegerField(default=0)),
                ('created_by', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_by'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('grade', models.CharField(max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BoardAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('best', models.BooleanField(null=True)),
                ('good', models.IntegerField(default=0)),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.boardquestion')),
            ],
            options={
                'ordering': ['created_by'],
            },
        ),
    ]
