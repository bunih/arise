from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.views import View
from .models import Believer, Location, Testimony
from .forms import UploadTestimonyForm
from django.contrib import messages
from django.core.paginator import Paginator


class MasterMixin:
    @property
    def process_data(self, filter_col=None, filter_data=None):
        _testimonies = Testimony.objects.filter(allowed=True).order_by('-uploaded_at')
        return _testimonies

    @property
    def testimonies(self, page_number=10, filter_data=None):
        filterItems = Paginator(self.process_data, page_number).get_page(self.request.GET.get('page'))
        return filterItems


class IndexView(View, MasterMixin):
    def get(self, *args, **kwargs):
        template_name = 'testimony/testimony.html'
        _form = UploadTestimonyForm()
        context = {
            'testimonies': self.testimonies,
            'form': _form
        }
        return render(self.request, template_name, context)
    @property
    def context_data(self):
        location_content = {
            'name': self.request.POST.get('location'),
            'country': self.request.POST.get('country'),
        }
        _locationInstance, info = Location.objects.get_or_create(**location_content)
        believer_content = {
            'name': self.request.POST.get('name'),
            'phone': self.request.POST.get('contact'),
            'location': _locationInstance,
        }
        _believerInstance, info = Believer.objects.get_or_create(**believer_content)
        context = {
            'title': self.request.POST.get('title'),
            'description': self.request.POST.get('description'),
            'user': self.request.user,
            'source': self.request.POST.get('source'),
            'category': self.request.POST.get('cat'),
            'believer': _believerInstance,
            'thumbnail': self.request.FILES.get('thumbnail'),
            'witness': self.request.POST.get('witness'),
            'witness_number': self.request.POST.get('witness_no'),
            'file': self.request.FILES.get('video'),
            'uploaded_at': self.request.POST.get('date'),
        }
        return context
    def post(self, *args, **kwargs):
        Testimony.objects.create(**self.context_data)
        messages.success(self.request, "Uploaded successfully!")
        return redirect("testimony:testimonies")





class SearchView(View):
    def get(self, *args, **kwargs):
        template_name = 'testimony/testimony.html'
        _form = UploadTestimonyForm()
        _q = self.request.GET.get('search')
        _testimonies = Testimony.objects.filter(allowed=True,title__icontains=_q).order_by('-created_at').distinct()

        filterItems = Paginator(_testimonies,10).get_page(self.request.GET.get('page'))
        context = {
            'testimonies': filterItems,
            'form': _form,
            'result':_testimonies.count
        }
        return render(self.request, template_name, context)



class ShowView(View):
    def get(self, *args, **kwargs):
        template_name = 'testimony/single_testimony.html'
        _slug = self.kwargs['slug']
        _testimony = Testimony.objects.filter(slug=_slug)[0]
        context = {
            'testimony': _testimony
        }
        return render(self.request, template_name, context)
