from django.conf.urls import url 

from . import views


app_name = "profile"
urlpatterns = [
    url(r'^dashboard', views.ProfileView.as_view(), name="dashboard")
]