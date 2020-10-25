from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
# path('books/', views.books, name='books'),
path('books/', views.BookListView.as_view(), name='books'),
path('authors/', views.AuthorListView.as_view(), name='authors'),
path('locations/', views.LocationListView.as_view(), name='locations')
]