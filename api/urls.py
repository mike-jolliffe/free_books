from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'location_books', views.LocationBookViewSet)
router.register(r'author_books', views.AuthorBookViewSet)

app_name = "api"
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]