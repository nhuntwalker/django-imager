"""imageshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView

from registration.backends.simple.views import RegistrationView

from . import views


urlpatterns = [
    url(r'^$',
        views.IndexView.as_view(),
        name="homepage"),

    url(r'^login/$',
        auth_views.login,
        {'template_name': 'login.html'},
        name="login"),

    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'logout.html'},
        name="logout"),

    url(r'^register/$',
        views.MyRegistration.as_view(), 
        name='register'),

    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='registration_closed.html'
        ),
        name='registration_disallowed'),

    url(r'^admin/',
        admin.site.urls),

    url(r'^profile/',
        include('imager_profile.urls')),

    url(r'^images/',
        include('imager_images.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
