# Generated by Django 3.2.5 on 2021-07-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_info',
            name='Email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher_info',
            name='Email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]