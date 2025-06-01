# DjangoClub/cju_club/urls.py

from django.contrib import admin
from django.urls import path, include
from club import views as club_views # club 앱의 views를 가져옴 (main.html을 위함)
from club.views import main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('club.urls', namespace='club')),  # main.html
    path('sign/', include('sign.urls')),  # 로그인/회원가입/로그아웃
    path('main/', main_view, name='main'),
    path('form/', include('form.urls')),
    path('form_list/', include('form_list.urls')),

    # 메인 페이지 URL (예: http://localhost:8000/)
    # club 앱에 main_page 뷰가 있다고 가정
     path('', club_views.main_view, name='main'), # '/' 경로를 club 앱의 main_page_view와 연결


]