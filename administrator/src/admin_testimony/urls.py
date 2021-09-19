from django.urls import path
from .views import *

urlpatterns=[
    path('',Index.as_view(),name='testimonies' ),
    path('remove__all_testimony/',remove__all_testimony,name='remove__all_testimony'),
    path('action/<slug:slug>',ActionView.as_view(),name='action_testimony'),
]