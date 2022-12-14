# Generated by Django 4.0.5 on 2022-08-02 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('endeavorapp', '0019_deck_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='wordincard',
            unique_together={('card', 'word')},
        ),
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_date', models.DateField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endeavorapp.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'card')},
            },
        ),
    ]
