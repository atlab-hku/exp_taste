# Generated by Django 3.0.10 on 2020-10-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201001_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='url',
            field=models.URLField(max_length=2000, unique=True, verbose_name='URL'),
        ),
    ]
