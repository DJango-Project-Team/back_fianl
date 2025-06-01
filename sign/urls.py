# DjangoClub/sign/urls.py

from django.urls import path
from . import views
from sign import views
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, logout_view

app_name = 'sign'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  # ← 여기!
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
