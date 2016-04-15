from imager_images.models import Photo
from django.views.generic.detail import DetailView

class PhotoDetailView(DetailView):
    model = Photo
    template_name = "imager_images/photo_detail.html"