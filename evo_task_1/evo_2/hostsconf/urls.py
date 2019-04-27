from django.conf.urls import url
from .views import redirector

urlpatterns = [
    url(r'^(?P<path>.*)', redirector),
            ]
