from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUserAcct(AbstractBaseUser, PermissionsMixin):
    user_choice=[
        ("Employer","Employer"),
        ("Applicant","Applicant")
    ]
    email = models.EmailField(unique=True)
    password=models.CharField(min_length=5, max_length=20)
    phone_num=models.CharField(max_length=12)
    address=models.CharField(max_length=255)
    user_type=models.CharField(choices=user_choice, default="Applicant")






























    # user_type = [
    #     ("Employer", "Employer"),
    #     ("Applicant", "Applicant")
    # ]
    # email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # user_type = models.CharField(max_length=20, choices=user_type)
    # password = models.CharField(max_length=128)