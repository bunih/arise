from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from subscribe.models import Subscriber

class Index(View):
    template_name='subscribes/subscribe_index.html'

    def get(self,*args,**kwargs):
        subscribes=Subscriber.objects.order_by('-id')
        context={
            'subscribes':subscribes
        }
        return render(self.request,self.template_name,context)





def remove_subscribe(request,id):
    group=Subscriber.objects.filter(pk=id)
    group.delete()
    messages.success(request,'selected subscribe deleted successfully!')
    return redirect('administrator:subscribe')

def remove__all_subscribe(request):
    group=Subscriber.objects.all()
    group.delete()
    messages.success(request,'All subscribes deleted successfully!')
    return redirect('administrator:subscribe')