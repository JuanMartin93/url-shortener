from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KUrl

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortener/home.html", {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Arlety Cara de Pene",
            "form": the_form
        }
        return render(request, "shortener/home.html", context) # Try Django 1.8 & 1.9 http://joincfe.com/youtube

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Arlety Cara de Pene",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = KUrl.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"
    
        return render(request, template ,context)

class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = KUrl.objects.filter(shortcodeurl__iexact=shortcode)
        print("Qs: " , qs)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()

        if "http://" not in obj.url:
            obj.url = "http://" + obj.url
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

        