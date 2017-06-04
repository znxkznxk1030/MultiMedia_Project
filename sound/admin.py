from django.contrib import admin

from .models import Sound


# Register your models here.

class SoundAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sound, SoundAdmin)