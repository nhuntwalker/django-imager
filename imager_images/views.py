from imager_images.models import Photo, Album
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class PhotoDetailView(DetailView):
    model = Photo
    template_name = "imager_images/photo_detail.html"

class AlbumDetailView(DetailView):
    model = Album
    template_name = "imager_images/album_detail.html"


class LibraryListView(ListView):
    model = Photo
    template_name = "imager_images/library_list.html"

    def get_context_data(self, **kwargs):
        context = super(LibraryListView, self).get_context_data(**kwargs)
        context["album_list"] = Album.objects.all().filter(owner=self.request.user)
        context["default_cover"] = "media/album_placeholder.png"

        return context