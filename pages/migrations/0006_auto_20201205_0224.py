# Generated by Django 3.1.2 on 2020-12-05 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201203_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='book_authors', through='pages.Author_Book', to='pages.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='author_books', through='pages.Author_Book', to='pages.Author'),
        ),
    ]