from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .enums import EmploymentType
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

class Job(models.Model):
    title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    employment_type = models.CharField(max_length=50, choices=EmploymentType)
    description = models.TextField()
    created_by = models.ForeignKey(
        User, related_name="created_jobs", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title


