from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from club.models import Club
from form_list.models import UserApplication
from .forms import ApplicationFormModelForm

@login_required(login_url='/sign/login/')
def submit_application(request, club_id):
    club = Club.objects.get(id=club_id)

    if request.method == 'POST':
        form = ApplicationFormModelForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user  # 만약 user 필드가 있다면 추가
            application.club = club
            application.save()
            # UserApplication도 저장
            UserApplication.objects.create(
                user=request.user,
                club=club,
            )
            # 추가 처리 (messages 등)
            return render(request, 'form/apply.html', {'club': club, 'success': True, 'form': form})

    else:
        form = ApplicationFormModelForm()

    return render(request, 'form/apply.html', {'club': club, 'form': form})
