from  django.urls import path
from . import views



urlpatterns=[
    path('login/',views.LoginView.as_view(),name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('reset',views.reset,name='reset')
]