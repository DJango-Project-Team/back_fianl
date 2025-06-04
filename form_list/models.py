# form_list/models.py
from django.db import models
from django.conf import settings
from club.models import Club

class UserApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='user_applications')
    status = models.CharField(max_length=20, default='접수')
    submitted_at = models.DateTimeField(auto_now_add=True)  # 신청일

    def __str__(self):
        return f"{self.user} - {self.club.name}"
