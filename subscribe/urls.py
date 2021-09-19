from django.urls import path
from .views import *

app_name='subscribe'
urlpatterns = [
    path('', IndexView.as_view(),name='subscribe'),
]
