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
    profile_picture = models.ImageField(
        upload_to='recruiter_pictures',
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.company_name}'


class Address(models.Model):
    class Meta:
        verbose_name_plural = 'Addresses'

    address_line1 = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    address_line2 = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    postal_code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    recruiter = models.OneToOneField(
        RecruiterProfile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.city} {self.postal_code}'


class Contacts(models.Model):
    class Meta:
        verbose_name_plural = 'Contacts'

    phone = models.CharField(
        max_length=12,
        null=True,
        blank=True,
    )
    linkedin_profile = models.URLField(
        null=True,
        blank=True,
    )
    facebook_profile = models.URLField(
        null=True,
        blank=True,
    )
    instagram_profile = models.URLField(
        null=True,
        blank=True,
    )
    twitter_profile = models.URLField(
        null=True,
        blank=True,
    )
    recruiter = models.OneToOneField(
        RecruiterProfile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.phone}'