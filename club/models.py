from django.db import models

# Create your models here.
class Club(models.Model):
    # 동아리 이름
    name = models.CharField(max_length=100)
    # 동아리 분과
    part = models.CharField(max_length=100)
    # 동아리 설명
    description = models.TextField()
    # id INT PRIMARY KEY AUTO_INCREMENT, 이 경우 자동으로 지정됨

    def __str__(self):
        return self.name

