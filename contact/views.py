from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Contact


class IndexView(View):
    def get(self, *args, **kwargs):
        template_name = 'contact/contact.html'
        return render(self.request, template_name)

    def post(self, *args, **kwargs):
        data = {
            "name": self.request.POST.get('name'),
            "phone": self.request.POST.get('phone'),
            "location": self.request.POST.get('location'),
            "email": self.request.POST.get('email'),
            "message": self.request.POST.get('message')
        }
        Contact.objects.create(**data)
        messages.success(
            self.request, f'Thank you {data["name"]}! Your message has been sent successfully!')
        return redirect('contact:contact')
