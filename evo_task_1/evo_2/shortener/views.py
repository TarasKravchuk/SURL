from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import ShortSURL
from .forms import SubmitURLForm
from analityc.models import ClickEvent
# Create your views here.


def home_view_post (request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'shortener/home.html', {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitURLForm(request.POST)
        context = {
            'title' : 'www.myshorturl.com',
            'form' : the_form}
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        context = {
            "title": "www.myshorturl.com",
            "form": form,
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortSURL.objects.create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/succes.html"
            else:
                template = "shortener/already-exist.html"

        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = ShortSURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
