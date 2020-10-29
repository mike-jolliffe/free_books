# Generated by Django 3.1.2 on 2020-10-25 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201024_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', through='pages.Author_Book', to='pages.Book'),
        ),
        migrations.AlterField(
            model_name='location',
            name='books',
            field=models.ManyToManyField(related_name='locations', through='pages.Location_Book', to='pages.Book'),
        ),
    ]