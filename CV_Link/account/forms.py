from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms

from CV_Link.profile_recruiter.models import RecruiterProfile
from CV_Link.profile_talent.models import TalentProfile

UserModel = get_user_model()


class RegisterAccountForm(auth_forms.UserCreationForm):
    ROLES = (
        ('Talent', 'Talent'),
        ('Recruiter', 'Recruiter'),
    )
    account_type = forms.ChoiceField(
        choices=ROLES,
        widget=forms.RadioSelect,
        required=True,
        initial='Talent'
    )

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', 'account_type']

    def save(self, commit=True):
        user = super().save(commit)
        profile = None
        if user.account_type == 'Talent':
            profile = TalentProfile(
                user=user
            )
        elif user.account_type == 'Recruiter':
            profile = RecruiterProfile(
                user=user
            )
        if profile and commit:
            profile.save()
        return user
