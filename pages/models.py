from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT)
    publicationDate = models.DateField()
    # coverImage = 

    def __str__(self):
        return self.name

class Author(models.Model):
    lastName = models.CharField(max_length=60)
    firstName = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"