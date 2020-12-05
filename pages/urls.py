from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('books/<int:book_pk>/<int:location_pk>', views.BookLocationUpdateView.as_view(), name='book-location-update-form'),
path('books/', views.BookListView.as_view(), name='books'),
path('books/create', views.BookCreateView.as_view(), name='book-create-form'),
path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
path('books/<int:pk>/update', views.BookUpdateView.as_view(), name='book-update-form'),
path('books/<int:book_pk>/update/<int:location_pk>', views.BookLocationUpdateView.as_view(), name='book-location-update-form'),
path('books/<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete-form'),
path('books/<int:book_pk>/delete/<int:location_pk>', views.BookLocationDeleteView.as_view(), name='book-location-delete-form'), 
path('authors/', views.AuthorListView.as_view(), name='authors'),
path('authors/create', views.AuthorCreateView.as_view(), name='author-create-form'),
path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
path('authors/<int:pk>/update', views.AuthorUpdateView.as_view(), name='author-update-form'),
path('authors/<int:pk>/delete', views.AuthorDeleteView.as_view(), name='author-delete-form'), 
path('locations/', views.LocationListView.as_view(), name='locations'),
path('locations/create', views.LocationCreateView.as_view(), name='location-create-form'),
path('locations/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
path('locations/<int:location_pk>/addBook', views.BookLocationCreateView.as_view(), name='location-book-create-form'),
path('locations/<int:pk>/update', views.LocationUpdateView.as_view(), name='location-update-form'),
path('locations/<int:location_pk>/update/<int:book_pk>', views.BookLocationUpdateView.as_view(), name='location-book-update-form'),
path('locations/<int:pk>/delete', views.LocationDeleteView.as_view(), name='location-delete-form'), 
path('locations/<int:location_pk>/delete/<int:book_pk>', views.BookLocationDeleteView.as_view(), name='location-book-delete-form'),
]