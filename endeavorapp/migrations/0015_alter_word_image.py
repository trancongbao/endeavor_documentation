# Generated by Django 4.0.5 on 2022-07-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endeavorapp', '0014_alter_word_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
