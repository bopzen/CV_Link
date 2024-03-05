from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins as auth_mixins

from CV_Link.profile_talent.models import TalentProfile, Education


class TalentDashboardView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    model = TalentProfile
    template_name = 'talent-profile-dashboard.html'
    context_object_name = 'talent_profile'

    def get_object(self, queryset=None):
        return TalentProfile.objects.get(user_id=self.request.user)


class TalentEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = TalentProfile
    template_name = 'talent-profile-edit.html'
    fields = ['first_name', 'last_name', 'birth_date', 'city', 'introduction']

    def get_object(self, queryset=None):
        return TalentProfile.objects.get(user_id=self.request.user)

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')


class TalentEducationCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = Education
    template_name = 'talent-education-create.html'
    fields = ['institution', 'degree', 'field_of_study', 'city', 'country', 'description', 'start_date', 'end_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')

    def form_valid(self, form):
        form.instance.talent = TalentProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class TalentEducationEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = Education
    template_name = 'talent-education-edit.html'
    fields = ['institution', 'degree', 'field_of_study', 'city', 'country', 'description', 'start_date', 'end_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')

    def form_valid(self, form):
        form.instance.talent = TalentProfile.objects.get(user=self.request.user)
        return super().form_valid(form)