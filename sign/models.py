from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#auth_user
class UserManager(BaseUserManager):
    def create_user(self, student_id, name, email, password=None):
        if not student_id:
            raise ValueError("학번은 필수입니다.")
        user = self.model(
            student_id=student_id,
            name=name,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.name
