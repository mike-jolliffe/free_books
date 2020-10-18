from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('lastName')
    serializer_class = AuthorSerializer