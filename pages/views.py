from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import resolve, reverse
from django.views import generic
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .models import Author, Book, Author_Book, Location, Location_Book
from pages.forms import SignUpForm


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'

class BookDetailView(generic.DetailView):
    model = Book 
    template_name = 'book_detail.html'

class BookUpdateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.UpdateView):
    group_required = "InventoryManager"
    model = Book
    fields = ['title', 'publicationDate', 'summary', 'language', 'genre', 'coverImage', 'authors']
    template_name = 'book_update_form.html'

class BookCreateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.CreateView):
    group_required = "InventoryManager"
    model = Book
    fields = ['title', 'publicationDate', 'summary', 'language', 'genre', 'coverImage', 'authors']
    template_name = 'book_create_form.html'

class BookDeleteView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.DeleteView):
    group_required = "InventoryManager"
    model = Book
    template_name = 'book_delete_form.html'
    success_url = '/books'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

class AuthorUpdateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.UpdateView):
    group_required = "InventoryManager"
    model = Author
    fields = ['lastName', 'firstName', 'authorImage', 'books']
    template_name = 'author_update_form.html'

class AuthorCreateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.CreateView):
    group_required = "InventoryManager"
    model = Author
    fields = ['lastName', 'firstName', 'authorImage', 'books']
    template_name = 'author_create_form.html'

class AuthorDeleteView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.DeleteView):
    group_required = "Inventory Manager"
    model = Author
    template_name = 'author_delete_form.html'
    success_url = '/authors'

class AuthorBookCreateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.CreateView):
    '''Associating a book to an author'''
    group_required = "Inventory Manager"
    model = Author_Book
    fields = ['book']
    template_name = 'author_book_create_form.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Ipsum` instance exists
        before going any further.
        """
        self.author = get_object_or_404(Author, pk=kwargs['author_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Overridden to add the ipsum relation to the `Lorem` instance.
        """
        form.instance.author = self.author
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('author-detail', args=str(self.kwargs['author_pk']))

class LocationListView(generic.ListView):
    model = Location
    template_name = 'location_list.html'

class LocationDetailView(generic.DetailView):
    model = Location
    template_name = 'location_detail.html'

class LocationUpdateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.UpdateView):
    group_required = "InventoryManager"
    model = Location
    fields = ['facilityName', 'city', 'state']
    template_name = 'location_update_form.html'

class LocationCreateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.CreateView):
    group_required = "InventoryManager"
    model = Location
    fields = ['facilityName', 'city', 'state']
    template_name = 'location_create_form.html'

class LocationDeleteView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.DeleteView):
    group_required = "InventoryManager"
    model = Location
    template_name = 'location_delete_form.html'
    success_url = '/locations'

class BookLocationCreateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.CreateView):
    '''Associating a book to a location'''
    group_required = "InventoryManager"
    model = Location_Book
    fields = ['book', 'quantity']
    template_name = 'location_book_create_form.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Ipsum` instance exists
        before going any further.
        """
        self.location = get_object_or_404(Location, pk=kwargs['location_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Overridden to add the ipsum relation to the `Lorem` instance.
        """
        form.instance.location = self.location
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('location-detail', args=str(self.kwargs['location_pk']))

class BookLocationUpdateView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.UpdateView):
    '''Updating quantity within the books route'''
    group_required = "InventoryManager"
    model = Location_Book
    fields = ['book','location','quantity']
    template_name = 'book_location_update_form.html'
    
    def calling_route(self):
        '''Determine which URL called this so the correct detail page can be returned'''
        current_url = self.request.build_absolute_uri('?')
        print(current_url)
        if 'books' in current_url:
            return 'books'
        else:
            return 'locations'

    def get_object(self, *args, **kwargs):
        obj = Location_Book.objects.get(book_id=self.kwargs['book_pk'], location_id=self.kwargs['location_pk'])
        return obj 

    def get_success_url(self):
        caller = self.calling_route()
        if caller == 'books':
            return reverse('book-detail', args=str(self.kwargs['book_pk']))
        else:
            return reverse('location-detail', args=str(self.kwargs['location_pk']))

class BookLocationDeleteView(LoginRequiredMixin, GroupRequiredMixin, generic.edit.DeleteView):
    '''Removing book from list at given location'''
    group_required = "InventoryManager"
    model = Location_Book
    fields = ['book','location','quantity']
    template_name = 'book_location_delete_form.html'
    
    def calling_route(self):
        '''Determine which URL called this so the correct detail page can be returned'''
        current_url = self.request.build_absolute_uri('?')
        print(current_url)
        if 'books' in current_url:
            return 'books'
        else:
            return 'locations'

    def get_object(self, *args, **kwargs):
        print(self.kwargs)
        #get route
        obj = Location_Book.objects.get(book_id=self.kwargs['book_pk'], location_id=self.kwargs['location_pk'])
        return obj 

    def get_success_url(self):
        caller = self.calling_route()
        if caller == 'books':
            return reverse('book-detail', args=str(self.kwargs['book_pk']))
        else:
            return reverse('location-detail', args=str(self.kwargs['location_pk']))

# @permission_required('polls.add_choice')

    