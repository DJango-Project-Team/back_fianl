# form/models.py
from django.db import models
from club.models import Club

class Application(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    motivation = models.TextField()
    spec = models.TextField()
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)  # 또는 ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
