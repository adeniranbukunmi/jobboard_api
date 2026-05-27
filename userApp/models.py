from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.


class CustomUserAcct(AbstractBaseUser, PermissionsMixin):
    user_type = [
        ("Employer", "Employer"),
        ("Applicant", "Applicant")
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=20, choices=user_type)