from django.db import models
from PIL import Image

# Create your models here.

# custom model manager
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')

# helper functions
def get_image_path(instance, filename):
    return '/'.join(['uploads/images', instance.upload.slug, filename])

# models
class Upload(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    image = models.ImageField(upload_to=get_image_path)
    status = models.Charfield(max_length=10, choices=STATUS_CHOICES, default='draft')


    published = PublishManager()
    objects = models.Manager()

    # use PIL to change the image size
    # override save function
    def save(self, *args, *kwargs):
        super(Upload, self).save()

        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (2000, 2000)
            if i_width > 2000 or i_height > 2000:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)