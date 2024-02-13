from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import mixins as auth_mixins

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


class AccountLoginView(auth_views.LoginView):
    template_name = 'account-login.html'

    def get_success_url(self):
        return reverse_lazy('home-page')


class AccountLogoutPageView(generic.TemplateView):
    template_name = 'account-logout.html'


class AccountLogoutView(auth_views.LogoutView):
    template_name = 'account-logout-confirmation.html'


class AccountDeleteView(generic.DeleteView):
    model = UserModel
    template_name = 'account-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user != user:
            return redirect('home-page')

        return super().delete(request, *args, **kwargs)


class AccountPasswordChangeView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'account-change-password.html'
    success_url = reverse_lazy('change-password-confirmation')


class AccountPasswordChangeConfirmView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = 'account-change-password-confirmation.html'
