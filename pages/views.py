from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Author, Book, Location


def index(request):
    return render(request, 'index.html')

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'

class LocationListView(generic.ListView):
    model = Location
    template_name = 'location_list.html'


# @permission_required('polls.add_choice')

    