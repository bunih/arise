from django.shortcuts import render
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, *args, **kwargs):
        template_name = 'welcome.html'
        return render(self.request, template_name)
