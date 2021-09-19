from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from testimony.models import Testimony


class Index(View):
    template_name = 'testimony/testimony_index.html'

    def get(self, *args, **kwargs):
        subscribes = Testimony.objects.order_by('-id')
        context = {
            'subscribes': subscribes
        }
        return render(self.request, self.template_name, context)


class ActionView(View):
    def get(self,*args,**kwargs):
        _test=Testimony.objects.filter(slug=self.kwargs.get('slug'))[0]
        if _test.allowed:
            _test.allowed= False
            messages.success(self.request, "Disabled successfully!")
        else:
          _test.allowed=True
          messages.success(self.request, "Allowed successfully!")
        _test.save()
        return redirect("testimony:testimonies")

    def post(self,*args,**kwargs):
        _test=Testimony.objects.filter(slug=self.kwargs.get('slug'))
        _test.delete()
        messages.success(self.request, "Testimony Removed successfully!")
        return redirect("testimony:testimonies")




def remove__all_testimony(request):
    group = Testimony.objects.all()
    group.delete()
    messages.success(request, 'All subscribes deleted successfully!')
    return redirect('administrator:subscribe')
