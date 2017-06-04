from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from sound.models import Sound


class SoundDeleteView(DeleteView):
    model = Sound
    success_url = reverse_lazy('user_sound:list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
