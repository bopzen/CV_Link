from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class TalentProfile(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
