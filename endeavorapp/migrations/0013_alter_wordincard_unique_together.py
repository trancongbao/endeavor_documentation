# Generated by Django 4.0.5 on 2022-07-31 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endeavorapp', '0012_alter_wordincard_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wordincard',
            unique_together={('card', 'order')},
        ),
    ]
