# Generated by Django 4.0.5 on 2022-07-28 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endeavorapp', '0002_alter_deckmodel_options_cardmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardmodel',
            name='current_interval',
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='deadline',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='cardmodel',
            name='study_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cardmodel',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='endeavorapp.deckmodel'),
        ),
        migrations.AlterField(
            model_name='cardmodel',
            name='front',
            field=models.TextField(max_length=500),
        ),
    ]
