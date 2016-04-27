from imager_images.models import Photo, Album
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView

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

# ---------- Create Items ----------

class PhotoCreationView(CreateView):
    model = Photo
    fields = ["image", "title", "description", "published"]
    template_name = "imager_images/create_photo.html"
    success_url = "/images/library"

    def form_valid(self, form, *args, **kwargs):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super(PhotoCreationView, self).form_valid(form)

class AlbumCreationView(CreateView):
    model = Album
    fields = ["title", "description", "photo_set", "published"]
    template_name = "imager_images/create_album.html"
    success_url = "/images/library"

    def form_valid(self, form, *args, **kwargs):
        """
        If the form is valid, save the associated model.
        """
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super(AlbumCreationView, self).form_valid(form)