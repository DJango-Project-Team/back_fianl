# form_list/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserApplication
from form.models import Application

@login_required
def application_detail_view(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if application.user != request.user:
        return redirect('form_list:my_applications')  # 본인 것이 아님

    return render(request, 'form_list/application_detail.html', {
        'application': application
    })



@login_required(login_url='/sign/login/')
def my_applications_view(request):
    applications = UserApplication.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'form_list/application_list.html', {
        'applications': applications,
    })
