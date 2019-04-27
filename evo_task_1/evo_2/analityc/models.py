from django.db import models
from shortener.models import ShortSURL


class ClickEventManager(models.Manager):
    def create_event(self, _Instance):
        if isinstance(_Instance, ShortSURL):
            obj, created = self.get_or_create(url=_Instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    event_url    = models.OneToOneField(ShortSURL, on_delete=None)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)

