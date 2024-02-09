from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms

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
        fields = ['username', 'email',]
