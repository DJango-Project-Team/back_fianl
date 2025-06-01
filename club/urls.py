# club/urls.py

from django.urls import path
from . import views

app_name = 'club'
# club 앱에서auth_permission url요청이 어떤 뷰와 연결되는지 설정
urlpatterns = [
    path('', views.main_view, name='main'),  # 루트 경로를 메인 뷰로 설정
    path('main', views.main_view, name='main'),  # 메인 페이지
    path('club/<int:club_id>/', views.club_detail_view, name='club_detail'),
    # path('apply/<int:club_id>/', views.apply_club_view, name='apply_club'),  # ✅ 이 줄이 필요
  # 세부 페이지 (추후 구현)
    #path('application_history/', views.application_history_view, name='application_history'),
]
