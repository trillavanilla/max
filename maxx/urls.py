from django.conf.urls import url, include
from django.contrib import admin
from maxx import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls, name='admin'),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('home/', include('home.urls', namespace='home')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
