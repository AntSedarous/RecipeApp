from django.db import models
from django.contrib import auth
# Create your models here.
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from annoying.fields import AutoOneToOneField
from django.urls import reverse_lazy

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
            # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


class UserAccount(models.Model):
    user = AutoOneToOneField(auth.models.User, related_name='profInfo', on_delete=models.CASCADE, primary_key=True)
    profilePic = models.ImageField(blank=True, upload_to=UploadToPathAndRename('images'), null=True )
    aboutMe = models.CharField(blank=True, default='', max_length = 300)
    pkk = models.IntegerField(editable=False)
    def __str__(self):
        return "@{}".format(self.user.username)

    def save(self, *args, **kwargs):
        self.pkk=self.user.pk
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse_lazy('recipies:by_recipe', kwargs={'username': self.user.username})
