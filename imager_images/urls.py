from django.conf.urls import url

from .views import (LibraryListView, PhotoDetailView, AlbumDetailView,
                    PhotoCreationView, AlbumCreationView)


app_name = "images"
urlpatterns = [
    url(r'^library', 
        LibraryListView.as_view(), name="library"),
    url(r'^photos/(?P<pk>[0-9]+)',
        PhotoDetailView.as_view(), name="single_photo"),
    url(r'^photos/add/$', 
        PhotoCreationView.as_view(), name="create_single_photo"),
    url(r'^albums/(?P<pk>[0-9]+)',
        AlbumDetailView.as_view(), name="single_album"),
    url(r'^albums/add/$', 
        AlbumCreationView.as_view(), name="create_single_album"),
]
