# Generated by Django 3.0.3 on 2020-03-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_question', '0004_auto_20200317_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionimage',
            name='image',
            field=models.URLField(),
        ),
    ]
