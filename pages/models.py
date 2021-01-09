import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
    class Meta:
         db_table = 'auth_user'
         app_label = 'auth'

    phone_number = models.CharField(max_length=50, null=True, blank=True, default="000-000-0000")
    bio = models.TextField()

# Create your models here.
class Book(models.Model):
    
    class Meta:
        db_table = 'pages_book'
        constraints = [
            models.UniqueConstraint(fields=['title', 'publicationDate'], name='unique title and date')
        ]
    
    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year+5    )):
        YEAR_CHOICES.append((r,r))
    title = models.CharField(max_length=255)
    publicationDate = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year, blank=True)
    summary = models.TextField(max_length=3000, blank=True)
    language = models.CharField(max_length=30, blank=True)
    genre = models.CharField(max_length=60, blank=True)
    coverImage = models.ImageField(upload_to='images/books/', blank=True)
    authors = models.ManyToManyField('Author', through='Author_Book', related_name='author_books', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    
    class Meta:
        db_table = 'pages_author'
        constraints = [
            models.UniqueConstraint(fields=['lastName', 'firstName'], name='unique last and first name')
        ]
    
    lastName = models.CharField(max_length=60)
    firstName = models.CharField(max_length=30)
    books = models.ManyToManyField('Book', through='Author_Book', related_name='book_authors', blank=True)
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
    locationImage = models.ImageField(upload_to='images/locations/', blank=True)

    def __str__(self):
        return f"{self.facilityName} - {self.city}, {self.state}"

    def get_absolute_url(self):
        return reverse('location-detail', args=[str(self.id)])

# Bridge table for Location and Book
class Location_Book(models.Model):
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.IntegerField(validators = [validators.MinValueValidator(0)])

    @staticmethod
    def getQuantity (book, location): 
        location_book = Location_Book.objects.get(book=book, location=location) 
        return location_book.quantity

# Bridge table for Author and Book 
class Author_Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
