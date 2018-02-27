from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Like)
admin.site.register(models.Recipe)
admin.site.register(models.Save)
