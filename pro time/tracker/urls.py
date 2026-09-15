from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import ProLoginView,dashboard,register
urlpatterns=[path('',dashboard,name='dashboard'),path('login/',ProLoginView.as_view(),name='login'),path('register/',register,name='register'),path('logout/',LogoutView.as_view(),name='logout'),path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset')]