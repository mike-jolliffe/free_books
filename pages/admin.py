from django.contrib import admin

# Register your models here.
from .models import Book, Author, Location
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Location)