from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class ActiveUserManager(models.Manager):
    """Convenience manager which returns only active profiles"""

    def get_queryset(self):
        queryset = super(ActiveUserManager, self).get_queryset()
        return queryset.filter(user__is_active__exact=True)


class ImagerProfile(models.Model):
    """Model for the profile of a given user."""
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
        null=False
    )

    camera_model = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    photography_type = models.CharField(max_length=255)
    friends = models.ManyToManyField(User,
                                     related_name='friend_of')

    objects = models.Manager()
    active = ActiveUserManager()

    def __str__(self):
        """Return string output of username."""
        return self.user.get_full_name() or self.user.username

    @property
    def is_active(self):
        """Return a boolean value indicating if 
        the profile's user is active."""
        return self.user.is_active

PHOTOGRAPHY_TYPES = [
    ('portrait', 'Portrait'),
    ('landscape', 'Landscape'),
    ('sports', 'Sports'),
]

US_REGIONS = [
('pnw', 'Pacific Northwest'),
('ne', 'New England'),
('ma', 'Mid-Atlantic'),
('se', 'Southeast'),
('mw', 'Midwest'),
('ds', 'Deep South'),
('sw', 'Southwest'),
('cf', 'California'),
('ak', 'Alaska'),
('hi', 'Hawaii'),
]

# ------------ Receivers ---------
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def ensure_profile_exists_on_user_save(sender, **kwargs):
    if kwargs.get("created", False):
        ImagerProfile.objects.get_or_create(user=kwargs.get("instance"))

