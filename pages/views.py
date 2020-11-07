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

class BookDetailView(generic.DetailView):
    model = Book 
    template_name = 'book_detail.html'

class BookUpdateView(generic.edit.UpdateView):
    model = Book
    fields = ['title', 'publicationDate', 'summary', 'language', 'genre', 'coverImage']
    template_name = 'book_update_form.html'

class BookCreateView(generic.edit.CreateView):
    model = Book
    fields = ['title', 'publicationDate', 'summary', 'language', 'genre', 'coverImage']
    template_name = 'book_create_form.html'

class BookDeleteView(generic.edit.DeleteView):
    model = Book
    template_name = 'book_delete_form.html'
    success_url = '/books'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

class AuthorUpdateView(generic.edit.UpdateView):
    model = Author
    fields = ['lastName', 'firstName', 'authorImage']
    template_name = 'author_update_form.html'

class AuthorCreateView(generic.edit.CreateView):
    model = Author
    fields = ['lastName', 'firstName', 'authorImage']
    template_name = 'author_create_form.html'

class AuthorDeleteView(generic.edit.DeleteView):
    model = Author
    template_name = 'author_delete_form.html'
    success_url = '/authors'

class LocationListView(generic.ListView):
    model = Location
    template_name = 'location_list.html'

class LocationDetailView(generic.DetailView):
    model = Location
    template_name = 'location_detail.html'

class LocationUpdateView(generic.edit.UpdateView):
    model = Location
    fields = ['facilityName', 'city', 'state']
    template_name = 'location_update_form.html'

class LocationCreateView(generic.edit.CreateView):
    model = Location
    fields = ['facilityName', 'city', 'state']
    template_name = 'location_create_form.html'

class LocationDeleteView(generic.edit.DeleteView):
    model = Location
    template_name = 'location_delete_form.html'
    success_url = '/locations'

# @permission_required('polls.add_choice')

    