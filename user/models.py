from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


# extend the user model
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def publish(self):
        self.published_date = timezone.now()
        self.save()