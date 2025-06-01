from django.shortcuts import render, get_object_or_404
from .models import Club

# 사용자 요청시 db에서 동아리 목록을 불러옴
# 사용자 해당 경로 접근 -> main_view() 함수 실행 -> main.html에 clubs 리스트 전달 -> 랜더링 결과 반환
def main_view(request):
    clubs = Club.objects.all()
    is_logged_in = request.user.is_authenticated  # 로그인 여부 체크

    return render(request, 'club/main.html', {
        'clubs': clubs,
        'is_logged_in': is_logged_in,
        'user': request.user if is_logged_in else None
    })

def club_detail_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    return render(request, 'club/detail.html', {'club': club})

# def apply_club_view(request, club_id):
#     # 예시: 신청서 양식을 띄우거나 처리
#     return render(request, 'club/apply.html', {'club_id': club_id})
