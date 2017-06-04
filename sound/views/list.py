from django.views.generic.list import ListView
from sound.models import Sound


class SoundListView(ListView):
    model = Sound
    template_name = 'sound/list.html'
    context_object_name = 'sounds'
    paginate_by = 5
