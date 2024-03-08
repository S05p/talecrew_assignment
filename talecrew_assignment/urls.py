from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from talecrew_assignment import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('posts.urls')),
] + static(settings.MEDIA_URL,document_ROOT=settings.MEDIA_ROOT)
