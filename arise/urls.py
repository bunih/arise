from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('contact/',include('contact.urls')),
    path('accounts/',include('accounts.urls')),
    path('subscribe/',include('subscribe.urls')),
    path('testimonies/',include('testimony.urls')),
    path('administrator/',include('administrator.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
