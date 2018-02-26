from django.db import models
from django.contrib import auth
# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(auth.models.User, related_name='profInfo', on_delete=models.CASCADE)
    profilePic = models.ImageField(blank=True, upload_to='images', null=True )

    def __str__(self):
        return "@{}".format(self.user.username)
