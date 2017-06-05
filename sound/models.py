from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.contrib.auth.models import User


# Create your models here.

class Sound(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField('Sound Description', blank=True)
    src = models.FileField(storage=FileSystemStorage(settings.MEDIA_ROOT),
                           default='settings.MEDIA_ROOT/example.mp3',
                           upload_to='user_sound')
    author = models.ForeignKey(User, default=1)

    def __str__(self):
        return self.name
