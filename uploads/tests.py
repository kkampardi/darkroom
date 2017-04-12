from django.test import TestCase

from .models import Image

# Models
class ModelTestCase(TestCase):
    # define a test suit for the Images Model

    def setUp(self):
        self.image_title = "Image One"
        self.image = Image(title="image_title")


    def test_model_can_create_an_object(self):
        objects_count = Image.objects.count()
        self.image.save()
        objects_new_count = Image.objects.count()
        self.assertNotEqual(objects_count, objects_new_count)

