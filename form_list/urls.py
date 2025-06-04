# form_list/urls.py
from django.urls import path
from . import views
from .views import my_applications_view

app_name = 'form_list'

urlpatterns = [
    path('list/', my_applications_view, name='application_list'),
]