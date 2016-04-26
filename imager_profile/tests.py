from django.contrib.auth.models import User
from django.test import TestCase
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


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user.set_password("secret123")

        self.user2 = UserFactory.build()
        self.user2.set_password("banana4")

    def tearDown(self):
        pass

    def test_user_creation(self):
        self.assertTrue(User.objects.count() == 0)
        self.user.save()
        self.assertTrue(User.objects.count() == 1)

    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(ImagerProfile.objects.count() == 0)
        self.user.save()
        self.assertTrue(ImagerProfile.objects.count() == 1)

    def test_profile_is_deleted_when_user_is_deleted(self):
        self.user.save()
        self.assertTrue(ImagerProfile.objects.count() == 1)
        self.user.delete()
        self.assertTrue(ImagerProfile.objects.count() == 0)

    def test_profile_str_is_user_username(self):
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def test_profile_has_appropriate_attributes(self):
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        for attr in ["photography_type", "location", "camera_model", "friends"]:
            self.assertTrue(attr in dir(profile))

    def test_profile_is_instance(self):
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        self.assertIsInstance(profile, ImagerProfile)

    def test_profile_friends(self):
        self.user.save()
        self.user2.save()
        self.assertTrue(self.user.profile.friends.count() == 0)
        self.user.profile.friends.add(self.user2)
        self.assertTrue(self.user.profile.friends.count() == 1)
        self.assertTrue(self.user2 in self.user.profile.friends.all())

    def test_profile_has_camera(self):
        self.user.save()
        self.assertEqual(self.user.profile.camera_model, "")
        self.user.profile.camera_model = "Panasonic"
        self.assertEqual(self.user.profile.camera_model, "Panasonic")
