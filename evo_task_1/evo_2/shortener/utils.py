import random, string
from django.db import models
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 10)

def short_code_generator (size=SHORTCODE_MIN , chars=string.digits + string.ascii_lowercase):
    print("size  ==  ", size)
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode (instance, size=SHORTCODE_MIN):
    new_code = short_code_generator(size=size)
    #Klass = instance.__class__
    #qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    qs_exists = instance.__class__.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance, size=size)
    else:
        return new_code
