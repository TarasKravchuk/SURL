from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIRECT_URL = getattr(settings, 'DEFAULT_REDIRECT_URL', 'http://www.myshorturl.com:8000')

def redirector (request, path=None):
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + '/' + path
    return HttpResponseRedirect(new_url)
