from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=60) #pull into separate table later
    publicationDate = models.DateField()
    # coverImage = 

    def __str__(self):
        return self.name