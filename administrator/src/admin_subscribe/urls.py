from django.urls import path
from .views import *

urlpatterns=[
    path('',Index.as_view(),name='subscribe' ),
    path('remove_subscribe/<int:id>/',remove_subscribe,name='remove_subscribe'),
    path('remove__all_subscribe/',remove__all_subscribe,name='remove__all_subscribe'),
]