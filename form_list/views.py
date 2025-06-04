# form_list/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserApplication

@login_required(login_url='/sign/login/')
def my_applications_view(request):
    applications = UserApplication.objects.filter(user=request.user).order_by('submitted_at')

    return render(request, 'form_list/application_list.html', {
        'applications': applications,
    })
