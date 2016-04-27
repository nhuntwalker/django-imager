from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import (ProfileView, edit_profile)


app_name = "profile"
urlpatterns = [
    url(r'^$',
        login_required(ProfileView.as_view(), login_url="/login/"),
        name="dashboard"),

    url(r'^edit/$', edit_profile, name='edit_profile')
]
