# form/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ApplicationFormModelForm
from club.models import Club

@login_required(login_url="/sign/login/")  # 경로 수정
def apply_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    success = False

    if request.method == 'POST':
        form = ApplicationFormModelForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.club = club
            application.user = request.user  # 로그인된 사용자 정보 저장
            application.save()
            success = True
    else:
        form = ApplicationFormModelForm()

    return render(request, 'form/apply.html', {
        'form': form,
        'club': club,
        'success': success
    })
