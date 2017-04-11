from django.db import models
from django.conf import settings

from PIL import Image

# Create your models here.

# custom model manager
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')


class Image(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created')
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=300, blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    published = PublishManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()



""" helper functions
def get_image_path(instance, filename):
    return '/'.join(['uploads/images', instance.image.slug, filename])

class Upload(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    image = models.ForeignKey(Image, related_name='upload_images', on_delete=models.CASCADE )
    file = models.ImageField(upload_to=get_image_path)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    published = PublishManager()
    objects = models.Manager()

    # use PIL to change the image size
    # override save function
    # override upload image saving
    def save(self, *args, **kwargs):

        # override save function
        super(Upload, self).save(*args, **kwargs)
        # our new code
        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (2000, 2000)
            if i_width > 2000:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)

"""