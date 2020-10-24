# serializers.py
from rest_framework import serializers

from pages.models import Book, Author, Location, Location_Book, Author_Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'publicationDate')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'firstName', 'lastName')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'facilityName', 'city', 'state')

class LocationBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location_Book
        fields = ('id', 'location', 'book', 'quantity')

class AuthorBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author_Book
        fields = ('id', 'author', 'book')
