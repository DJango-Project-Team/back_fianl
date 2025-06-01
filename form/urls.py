# form/urls.py
from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('apply/<int:club_id>/', views.apply_view, name='apply_club'),
]
