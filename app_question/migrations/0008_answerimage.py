# Generated by Django 3.0.3 on 2020-03-27 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_question', '0007_auto_20200321_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('seq', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app_question.Answer')),
            ],
            options={
                'db_table': 'auswer_image',
            },
        ),
    ]