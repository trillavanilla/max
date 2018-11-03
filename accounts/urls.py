app_name='accounts'

from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.urls import path

urlpatterns = [

    path('login/', LoginView.as_view(template_name='accounts/login.html'),
    name='login'),

    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/(?P<pk>\d+)/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),

    path('password-reset/',
    PasswordResetView.as_view(template_name='accounts/password_reset.html',
    success_url=reverse_lazy('accounts:password_reset_done')),
    {'email_template_name': 'accounts/password_reset_email.html'},
    name='password_reset'),

    path('password-reset/done/',
    PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset/confirm/<uidb64>/<token>/',
    PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
    success_url=reverse_lazy('accounts:password_reset_complete')),
    name='password_reset_confirm'),

    path('password-reset/complete/',
    PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
    name='password_reset_complete'),

]
