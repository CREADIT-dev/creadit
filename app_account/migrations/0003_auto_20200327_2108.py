# Generated by Django 3.0.3 on 2020-03-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0002_auto_20200317_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='유저의 닉네임'),
        ),
    ]
