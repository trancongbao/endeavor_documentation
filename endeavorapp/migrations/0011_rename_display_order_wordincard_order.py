# Generated by Django 4.0.5 on 2022-07-31 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endeavorapp', '0010_alter_card_order_alter_wordincard_display_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordincard',
            old_name='display_order',
            new_name='order',
        ),
    ]
