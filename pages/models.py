from django.db import models
from django.core import validators


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    publicationDate = models.DateField()
    # coverImage = 

    def __str__(self):
        return self.name

class Author(models.Model):
    lastName = models.CharField(max_length=60)
    firstName = models.CharField(max_length=30)
    books = models.ManyToManyField('Book', through='Author_Book')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class Location(models.Model):
    facilityName = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=2)
    books = models.ManyToManyField('Book', through='Location_Book')

    def __str__(self):
        return f"{self.facilityName} - {self.city}, {self.state}"

# Bridge table for Location and Book
class Location_Book(models.Model):
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    quantity = models.IntegerField(validators = [validators.MinValueValidator(0)])

# Bridge table for Author and Book 
class Author_Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)