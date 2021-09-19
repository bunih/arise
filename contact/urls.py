from django.urls import path
from .views import *

app_name='contact'
urlpatterns = [
    path('', IndexView.as_view(),name='contact'),
]
