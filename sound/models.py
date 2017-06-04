from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


# Create your models here.

class Sound(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField('Sound Description', blank=True)
    src = models.FileField(storage=FileSystemStorage(settings.MEDIA_ROOT),
                           default='settings.MEDIA_ROOT/example.mp3',
                           upload_to='user_sound')

    def __str__(self):
        return self.name
