from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from CV_Link.account.managers import CustomUserManager


class AccountUser(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('Talent', 'Talent'),
        ('Recruiter', 'Recruiter'),
    )

    username = models.CharField(
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    account_type = models.CharField(
        max_length=20,
        choices=ROLES,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

