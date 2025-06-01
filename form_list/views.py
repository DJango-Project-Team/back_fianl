# form_list/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from form.models import Application

@login_required(login_url='/sign/login/')
def application_list_view(request):
    user_name = request.session.get('user_name')
    if not user_name:
        return redirect('/sign/login/')

    applications = Application.objects.all().order_by('id')  # 전체 보기 예시 (실제 사용자는 filter 필요)

    if not applications.exists():
        return render(request, 'form_list/list.html', {
            'applications': [],
            'message': '신청 내역이 없습니다.'
        })

    return render(request, 'form_list/list.html', {
        'applications': applications,
        'message': None
    })

@login_required(login_url='/sign/login/')
def application_detail_view(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    return render(request, 'form_list/detail.html', {'application': application})