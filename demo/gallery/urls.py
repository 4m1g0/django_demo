from django.conf.urls import url
from . import views

app_name = 'gallery' # important to include all names inside the namespace for templates. Example: gallery:index

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
]
