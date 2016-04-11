from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')

PUBLISH_OPTIONS = [("private", "Private"),
                   ("shared", "Shared"),
                   ("public", "Public")]


class Photo(models.Model):
    file = models.ImageField(upload_to='user_photos')
    owner = models.OneToOneField(User, related_name="photo", null=False, default=None)
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.CharField(
        max_length=7, choices=PUBLISH_OPTIONS, default="public")


class Album(models.Model):
    """A model that houses and points to many photos"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    photo_set = models.ManyToManyField(Photo, related_name="photos_of")
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.CharField(max_length=7, choices=PUBLISH_OPTIONS, default="public")


