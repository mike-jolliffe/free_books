# Generated by Django 3.1.2 on 2020-10-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20201025_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='authorImage',
            field=models.ImageField(blank=True, upload_to='images/authors/'),
        ),
    ]
