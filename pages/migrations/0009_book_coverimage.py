# Generated by Django 3.1.2 on 2020-10-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20201025_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='coverImage',
            field=models.ImageField(blank=True, upload_to='images/books/'),
        ),
    ]
