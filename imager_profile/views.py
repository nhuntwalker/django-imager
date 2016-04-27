from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ImagerProfile
from .forms import UserInfoForm, ProfileInfoForm

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

# ---------- Edit Profile ----------

# class ProfileEditView(UpdateView):
#     template_name = "imager_profile/edit_profile.html"
#     form_class = UserInfoForm
#     second_form_class = ProfileInfoForm
#     success_url = "/profile"

#     def get_context_data(self, **kwargs):
#         context = super(ProfileEditView, self).get_context_data(**kwargs)
#         if 'form' not in context:
#             context['form'] = self.form_class
#         if 'form2' not in context:
#             context['form2'] = self.second_form_class
#         return context

#     def get_object(self):
#         return self.request.user

#     def form_invalid(self, **kwargs):
#         return self.render_to_response(self.get_context_data(**kwargs))


def edit_profile(request):
    """Allow user to edit their ImagerProfile, and limited fields of User."""
    user = request.user
    profile = request.user.profile
    user_form = UserInfoForm(instance=user)
    profile_form = ProfileInfoForm(instance=profile)

    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=user)
        profile_form = ProfileInfoForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/profile')
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'imager_profile/edit_profile.html', context)
