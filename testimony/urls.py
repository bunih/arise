from django.urls import path,include
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from .views import IndexView, SearchView,ShowView


# ===========Normal View=====================
app_name="testimony"
urlpatterns=[
    path('',IndexView.as_view(),name='testimonies'),
    path('result/',SearchView.as_view(),name='filter'),
    path('show/<slug:slug>/',ShowView.as_view(),name='show'),
]