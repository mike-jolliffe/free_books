from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Author, Book, Location, Location_Book



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

class BookLocationUpdateView(generic.edit.UpdateView):
    model = Location_Book
    fields = ['book','location','quantity']
    template_name = 'book_location_update_form.html'
    
    def get_object(self, *args, **kwargs):
        # This method should return a queryset that represents the items to be listed in the view.
        # I think you intend on listing categories in your view, in which case consider changing the view's name to CategoryListView. Just sayin'...
        # An instance of this view has a dictionary called `kwargs` that has the url parameters, so you can do the following:

        # You need some null assertions here because of the way you've setup your URLs
        obj = Location_Book.objects.get(book_id=self.kwargs['book_pk'], location_id=self.kwargs['location_pk'])
        print(obj)
        return obj 

    def get_success_url(self):
        return reverse('book-detail', args=str(self.kwargs['book_pk']))
# @permission_required('polls.add_choice')

    