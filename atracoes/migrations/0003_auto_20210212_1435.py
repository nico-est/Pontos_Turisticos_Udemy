# Generated by Django 3.1.6 on 2021-02-12 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_auto_20210212_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atracao',
            old_name='horario_fund',
            new_name='horario_func',
        ),
    ]