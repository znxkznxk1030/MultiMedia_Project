from django.views.generic.base import TemplateView
from user.mixin import AdminRequiredMixin


class SoundNewView(AdminRequiredMixin, TemplateView):
    template_name = 'sound/new.html'
