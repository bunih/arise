from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from contact.models import Contact

class Index(View):
    template_name='contacts/contact_index.html'

    def get(self,*args,**kwargs):
        contacts=Contact.objects.order_by('-id')
        context={
            'contacts':contacts
        }
        return render(self.request,self.template_name,context)





def remove_contact(request,id):
    group=Contact.objects.filter(pk=id)
    group.delete()
    messages.success(request,'selected contact deleted successfully!')
    return redirect('administrator:contact')

def remove__all_contact(request):
    group=Contact.objects.all()
    group.delete()
    messages.success(request,'All contacts deleted successfully!')
    return redirect('administrator:contact')