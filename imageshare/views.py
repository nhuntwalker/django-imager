from django.shortcuts import render
from django.views.generic import TemplateView
from registration.backends.simple.views import RegistrationView

from imager_images.models import Photo

class IndexView(TemplateView):
    """View for the home page"""
    template_name = "index.html"
    # if user is logged in, go to profile. else, go to the index

    def get_context_data(self, **kwargs):
        """Pass an image to the homepage to serve as the background"""
        try:
            img = Photo.objects.filter(published="public").order_by("?")[0]
        except IndexError:
            img = "static/DSC_7749.JPG"

        context = super(IndexView, self).get_context_data(**kwargs)
        context["img"] = img
        return context

class MyRegistration(RegistrationView):
    """View for the registration page"""
    template_name = "register.html"
