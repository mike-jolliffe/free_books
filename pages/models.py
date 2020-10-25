import datetime
from django.db import models
from django.core import validators
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Book(models.Model):
    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year+5    )):
        YEAR_CHOICES.append((r,r))
    title = models.CharField(max_length=255)
    publicationDate = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, blank=True)
    summary = models.TextField(max_length=3000, blank=True)
    language = models.CharField(max_length=30, blank=True)
    genre = models.CharField(max_length=60, blank=True)
    coverImage = models.ImageField(upload_to='images/books/', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    # def getQtyAtLocation (self, location): 
    #     location_book = Location_Book.objects.get(book=self, location=location) 
    #     return location_book.quantity

class Author(models.Model):
    lastName = models.CharField(max_length=60)
    firstName = models.CharField(max_length=30)
    books = models.ManyToManyField('Book', through='Author_Book', related_name='authors')
    authorImage = models.ImageField(upload_to='images/authors/', blank=True)


    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
class Location(models.Model):
    facilityName = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=2)
    books = models.ManyToManyField('Book', through='Location_Book', related_name='locations')

    def __str__(self):
        return f"{self.facilityName} - {self.city}, {self.state}"

    def get_absolute_url(self):
        return reverse('location-detail', args=[str(self.id)])

# Bridge table for Location and Book
class Location_Book(models.Model):
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    quantity = models.IntegerField(validators = [validators.MinValueValidator(0)])

# Bridge table for Author and Book 
class Author_Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
