# Generated by Django 3.1.2 on 2020-10-21 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201021_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]
