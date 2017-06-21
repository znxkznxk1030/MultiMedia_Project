from django.views.generic.base import View
from django.shortcuts import redirect

from sound.models import Sound
from sound_process.cut_frequency import cutoff_frequency
from sound_process.pca_extraction import primary_extract
from sound_process.reverb import reverb
from user.mixin import AdminRequiredMixin


class SoundCreateView(AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        src = request.FILES.get('src')
        sound = Sound.objects.create(
            name=name,
            description=description,
            src=src,
        )
        # Sound.objects.select_for_update()
        redirect('user_sound:list')

        primary_extract()

        # cutoff_frequency()

        return redirect('user_sound:list')
