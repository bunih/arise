from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Subscriber


class IndexView(View):
    def post(self, *args, **kwargs):
        data = {
            "email": self.request.POST.get('email'),
        }
        Subscriber.objects.create(**data)
        messages.success(
            self.request, f'Thank you for subscribing our newlatter')
        return redirect('home:welcome')
