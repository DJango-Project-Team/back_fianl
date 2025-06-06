# form_list/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserApplication
from form.models import Application

@login_required(login_url='/sign/login/')
def application_detail_view(request, application_id):
    user_application = get_object_or_404(UserApplication, id=application_id, user=request.user)
    application = get_object_or_404(Application, user=request.user, club=user_application.club)

    return render(request, 'form_list/application_detail.html', {
        'application': application,
    })

# form_list/views.py

@login_required(login_url='/sign/login/')
def my_applications_view(request):
    applications = UserApplication.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'form_list/application_list.html', {
        'applications': applications,
    })
