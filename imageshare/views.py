from django.shortcuts import render
from django.views.generic import TemplateView

class ClassView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        return {}