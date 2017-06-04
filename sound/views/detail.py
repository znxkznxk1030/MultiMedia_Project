from django.views.generic.detail import DetailView
from sound.models import Sound


class SoundDetailView(DetailView):
    model = Sound
    template_name = 'sound/detail.html'
    context_object_name = 'sound'
