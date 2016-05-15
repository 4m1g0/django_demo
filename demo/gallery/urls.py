from django.conf.urls import url
from . import views

app_name = 'gallery' # important to include all names inside the namespace for templates. Example: gallery:index

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
