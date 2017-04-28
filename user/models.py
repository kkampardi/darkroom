from django.db import models
from django.conf import settings

# Create your models here.


# extend the user model
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

