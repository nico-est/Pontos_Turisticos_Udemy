# Generated by Django 3.1.6 on 2021-02-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0003_auto_20210212_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]
