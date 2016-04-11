from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Photo(models.Model):
    # file = models.ImageField(upload_to=user_directory_path, max_length=100)
    file = models.ImageField(upload_to='user_photos')

