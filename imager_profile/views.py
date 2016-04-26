from django.views.generic import DetailView
from django.shortcuts import render

from .models import ImagerProfile

# Create your views here.

class ProfileView(DetailView):
    template_name = "imager_profile/dashboard.html"
    model = ImagerProfile

    def get_object(self):
        return self.request.user

    def get_context_object(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["n_photos"] = len(self.request.user.photo.all())
        return context