from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class RecruiterProfile(models.Model):
    company_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    company_description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )
    company_website = models.URLField()
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.company_name}'
