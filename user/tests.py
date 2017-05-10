from django.test import TestCase

from .models import Profile

# Model test suit
class ModelTestCase(TestCase):

    def setUp(self):
        self.nick_name = "rockstar"
        self.profile = Profile(user="nick_name")

    def test_model_can_create_a_user(self):
        objects_count = Profile.objects.count()
        self.profile.save()
        objects_new_count = Profile.objects.count()
        self.assertNotEqual(objects_count, objects_new_count)