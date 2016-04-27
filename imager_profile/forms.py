from django import forms
from django.contrib.auth.models import User

from .models import ImagerProfile


class UserInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileInfoForm(forms.ModelForm):

    class Meta:
        model = ImagerProfile
        fields = ["camera_model", "location", "photography_type", "friends"]
