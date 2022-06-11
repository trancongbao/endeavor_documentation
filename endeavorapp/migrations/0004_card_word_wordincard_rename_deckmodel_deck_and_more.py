# Generated by Django 4.0.5 on 2022-07-31 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endeavorapp', '0003_remove_cardmodel_current_interval_cardmodel_deadline_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_date', models.DateField(null=True)),
                ('deadline', models.DateField(null=True)),
                ('front', models.TextField(max_length=500)),
                ('back', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(max_length=100)),
                ('pronunciation', models.TextField(max_length=100)),
                ('definition', models.TextField(max_length=500)),
                ('image', models.TextField(max_length=100)),
                ('video', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WordInCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.SmallIntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endeavorapp.card')),
                ('dict_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endeavorapp.word')),
            ],
        ),
        migrations.RenameModel(
            old_name='DeckModel',
            new_name='Deck',
        ),
        migrations.DeleteModel(
            name='CardModel',
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='endeavorapp.deck'),
        ),
    ]