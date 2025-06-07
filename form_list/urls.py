# form_list/urls.py
from django.urls import path
from . import views

app_name = 'form_list'

urlpatterns = [
    path('detail/<int:application_id>/', views.application_detail_view, name='application_detail'),
    path('my-applications/', views.my_applications_view, name='my_applications'),
]
