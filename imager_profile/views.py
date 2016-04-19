from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class ProfileView(TemplateView):
    template_name = "imager_profile/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

# def profile_view(request, *args, **kwargs):
#     context = {"args": args, "kwargs": kwargs}
#     the_template = "imager_profile/dashboard.html"
#     return render(request, the_template, context=context)