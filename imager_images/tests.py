from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
import factory
import pdb

from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(
        lambda n: "user{}".format(n)
    )
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo

    title = factory.Sequence(
        lambda n: "photo title {}".format(n)
    )
    description = factory.Sequence(
        lambda n: "some_photo_description"
    )


class AlbumFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Album


class AlbumPhotoTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user.set_password("secret123")
        self.user.save()

        self.photo = PhotoFactory.build()

    def tearDown(self):
        pass

    def test_photo_creation(self):
        self.assertTrue(Photo.objects.count() == 0)
        self.photo.owner = self.user
        self.photo.save()
        self.assertTrue(Photo.objects.count() == 1)

    def test_photo_deletion(self):
        self.photo.owner = self.user
        self.photo.save()
        self.assertTrue(Photo.objects.count() == 1)
        self.photo.delete()
        self.assertTrue(Photo.objects.count() == 0)

    def test_photo_ownership(self):
        self.photo.owner = self.user
        self.photo.save()
        self.assertTrue(self.photo.owner == self.user)

    def test_description_is_set(self):
        self.photo.owner = self.user
        self.photo.save()
        self.assertIsNotNone(self.photo.description)

    def test_photo_is_public(self):
        self.assertEqual(self.photo.published, "public")

    def test_photo_published_recently(self):
        self.assertIsNone(self.photo.date_published)
        self.photo.owner = self.user
        self.photo.save()
        self.assertLess(self.photo.date_published, timezone.now())
