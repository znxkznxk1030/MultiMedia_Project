from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', SoundListView.as_view(), name='list'),
    url(r'^create/$', SoundCreateView.as_view(), name='create'),
    url(r'^new/$', SoundNewView.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$', SoundDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', SoundDeleteView.as_view(), name='delete'),
]
