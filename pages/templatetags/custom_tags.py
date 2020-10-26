from django import template 
register = template.Library() 
from pages.models import Book, Location, Author, Location_Book, Author_Book 

@register.simple_tag 
def getQuantityAtLocation(book:Book, location:Location): 
    return Location_Book.objects.get(book=book, location=location).quantity