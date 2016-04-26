from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):
    name = 'imager_profile'
    verbose_name = "Imager User Profile"

    def ready(self):
        from imager_profile import signals