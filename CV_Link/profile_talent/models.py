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
    introduction = models.TextField(
        max_length=300,
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


class Education(models.Model):
    class Meta:
        verbose_name_plural = 'Education'

    institution = models.CharField(
        max_length=200,
    )
    field_of_study = models.CharField(
        max_length=200,
    )
    city = models.CharField(
        max_length=50,
    )
    country = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        max_length=300,
    )
    start_date = models.DateField()
    end_date = models.DateField()

    talent = models.ForeignKey(
        TalentProfile,
        on_delete=models.CASCADE,
    )


class WorkExperience(models.Model):
    class Meta:
        verbose_name_plural = 'Work Experience'

    company = models.CharField(
        max_length=200,
    )
    sector = models.CharField(
        max_length=200,
    )
    position = models.CharField(
        max_length=200,
    )
    city = models.CharField(
        max_length=50,
    )
    country = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        max_length=300,
    )
    start_date = models.DateField()
    end_date = models.DateField()

    talent = models.ForeignKey(
        TalentProfile,
        on_delete=models.CASCADE,
    )