from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins as auth_mixins

from CV_Link.profile_recruiter.models import RecruiterProfile, Address


class RecruiterDashboardView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    model = RecruiterProfile
    template_name = 'recruiter-profile-dashboard.html'
    context_object_name = 'recruiter_profile'

    def get_object(self, queryset=None):
        return RecruiterProfile.objects.get(user_id=self.request.user)


class RecruiterEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = RecruiterProfile
    template_name = 'recruiter-profile-edit.html'
    fields = ['company_name', 'company_description', 'company_website']

    def get_object(self, queryset=None):
        return RecruiterProfile.objects.get(user_id=self.request.user)

    def get_success_url(self):
        return reverse_lazy('recruiter-dashboard')


class RecruiterAddressEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = Address
    template_name = 'recruiter-address-edit.html'
    fields = ['address_line1', 'address_line2', 'city', 'postal_code', 'country']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recruiter'] = self.object.recruiter
        return context

    def get_success_url(self):
        return reverse_lazy('recruiter-dashboard')