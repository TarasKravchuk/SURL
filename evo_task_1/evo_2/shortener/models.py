from .utils import short_code_generator
from .validators import validate_dot_com, validate_url
from django.db import models
from django.conf import settings

# Create your models here.

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)

class URLManager (models. Manager):
    def all (self, *args, **kwargs):
        qs_main = super(URLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = ShortSURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
            #qs = qs.order_by('id')[:items]

        new_codes = 0
        for q in qs:
            q.shortcode = short_code_generator()
            q.save()
            new_codes += 1
        return f'New codes made {new_codes}'

class ShortSURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, null=False, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = URLManager()



    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = short_code_generator(self)
            if not "http" in self.url:
                self.url = "http://" + self.url
        super(ShortSURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_surl (self):
        return f'https://www.myshorturl.com/{self.shortcode}'

