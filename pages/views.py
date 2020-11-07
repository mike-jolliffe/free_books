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

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

class AuthorUpdateView(generic.edit.UpdateView):
    model = Author
    fields = ['lastName', 'firstName']
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

# @permission_required('polls.add_choice')

    