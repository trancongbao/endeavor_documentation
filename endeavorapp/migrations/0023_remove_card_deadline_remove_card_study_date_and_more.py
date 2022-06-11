# Generated by Django 4.0.5 on 2022-08-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endeavorapp', '0022_rename_usercard_studiedcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='card',
            name='study_date',
        ),
        migrations.AddField(
            model_name='card',
            name='words',
            field=models.ManyToManyField(through='endeavorapp.WordInCard', to='endeavorapp.word'),
        ),
    ]
