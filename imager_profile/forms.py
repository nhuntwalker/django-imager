from django import forms 
from django.contrib.auth.models import User

from .models import ImagerProfile

class AccountInfoForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ["first_name", "last_name"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ["camera_model", "location"]

    def get_context_data(self, **kwargs):
        context["profile"] = self.model.get()