from django.conf.urls import url 

from .views import (LibraryListView, PhotoDetailView, AlbumDetailView)


app_name = "images"
urlpatterns = [
    url(r'^library', LibraryListView.as_view(), name="dashboard"),
    url(r'^photos/(?P<pk>[0-9]+)', PhotoDetailView.as_view(), name="single_photo"),
    url(r'^albums/(?P<pk>[0-9]+)', AlbumDetailView.as_view(), name="single_album"),
]