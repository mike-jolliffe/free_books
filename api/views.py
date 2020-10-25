from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer, AuthorSerializer, LocationSerializer, LocationBookSerializer, AuthorBookSerializer
from pages.models import Book, Author, Location, Location_Book, Author_Book

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('lastName')
    serializer_class = AuthorSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('facilityName')
    serializer_class = LocationSerializer

class LocationBookViewSet(viewsets.ModelViewSet):
    queryset = Location_Book.objects.all().order_by('location', 'book')
    serializer_class = LocationBookSerializer

class AuthorBookViewSet(viewsets.ModelViewSet):
    queryset = Author_Book.objects.all().order_by('author')
    serializer_class = AuthorBookSerializer
