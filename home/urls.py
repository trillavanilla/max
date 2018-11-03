from django.urls import path, re_path
from home.views import HomeView
from . import views

app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
    views.change_friends, name='change_friends'),
    path('counter/', views.counter, name='counter'),
]
