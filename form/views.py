from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from club.models import Club
from form_list.models import UserApplication
from .forms import ApplicationFormModelForm

from .models import Application

@login_required(login_url='/sign/login/')
def submit_application(request, club_id):
    club = Club.objects.get(id=club_id)

    if request.method == 'POST':
        department = request.POST.get('department')
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        motivation = request.POST.get('motivation')
        spec = request.POST.get('spec')

        # 직접 저장
        Application.objects.create(
            user=request.user,
            club=club,
            department=department,
            student_id=student_id,
            name=name,
            email=email,
            motivation=motivation,
            spec=spec
        )
        UserApplication.objects.create(user=request.user, club=club)
        return render(request, 'form/apply.html', {
            'club': club,
            'success': True
        })
    return render(request, 'form/apply.html', {'club': club})


