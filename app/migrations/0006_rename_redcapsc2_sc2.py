# Generated by Django 5.0.4 on 2024-06-22 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_redcapsc2_laboratorio_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RedcapSC2',
            new_name='SC2',
        ),
    ]