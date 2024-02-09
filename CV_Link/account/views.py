from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, get_user_model, login

from CV_Link.account.forms import RegisterAccountForm

UserModel = get_user_model()


class AccountRegisterView(generic.CreateView):
    template_name = 'account-register.html'
    form_class = RegisterAccountForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result