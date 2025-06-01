# form_list/urls.py
from django.urls import path
from . import views

app_name = 'form_list'


urlpatterns = [
    path('list/', views.application_list_view, name='application_list'),
    path('detail/<int:application_id>/', views.application_detail_view, name='application_detail'),
]
