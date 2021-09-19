from django import forms
from .models import *
from django.contrib import messages

class UploadTestimonyForm(forms.ModelForm):
    class Meta:
        model =Testimony
        exclude=['team','slug','active']
        labels={
            'category':'choose or create Category',
            'total':'How many in Stock?',
        }