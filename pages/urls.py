from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
# path('books/', views.books, name='books'),
path('books/', views.BookListView.as_view(), name='books'),
path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
path('authors/', views.AuthorListView.as_view(), name='authors'),
path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
path('locations/', views.LocationListView.as_view(), name='locations'),
path('locations/<int:pk>', views.LocationDetailView.as_view(), name='location-detail')
]