from django.shortcuts import render
from django.http import HttpResponse
from .models import Author

# Create your views here.
def index(request):
    authors = Author.objects.all()
    print(authors)
    # Render the HTML template index.html
    return render(request, 'index.html', {'a': authors})