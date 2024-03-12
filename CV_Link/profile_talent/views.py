from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins as auth_mixins

from CV_Link.profile_talent.models import TalentProfile, Education, WorkExperience, TechStack


class TalentDashboardView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    model = TalentProfile
    template_name = 'talent-profile-dashboard.html'
    context_object_name = 'talent_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educations'] = TalentProfile.objects.get(user=self.request.user).education_set.order_by('-end_date')
        context['work_experiences'] = TalentProfile.objects.get(user=self.request.user).workexperience_set.order_by('-end_date')
        return context

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


class TalentEducationDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = Education
    template_name = 'talent-education-delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')


class TalentWorkExperienceCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = WorkExperience
    template_name = 'talent-work-experience-create.html'
    fields = ['company', 'sector', 'position', 'city', 'country', 'description', 'start_date', 'end_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')

    def form_valid(self, form):
        form.instance.talent = TalentProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class TalentWorkExperienceEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = WorkExperience
    template_name = 'talent-work-experience-edit.html'
    fields = ['company', 'sector', 'position', 'city', 'country', 'description', 'start_date', 'end_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')

    def form_valid(self, form):
        form.instance.talent = TalentProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class TalentWorkExperienceDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = WorkExperience
    template_name = 'talent-work-experience-delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')


class TalentTechStackCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    model = TechStack
    template_name = 'talent-tech-stack-create.html'
    fields = ['technologies']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')

    def form_valid(self, form):
        form.instance.talent = TalentProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class TalentTechStackEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = TechStack
    template_name = 'talent-tech-stack-edit.html'
    fields = ['technologies']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')

    def form_valid(self, form):
        form.instance.talent = TalentProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class TalentTechStackDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = TechStack
    template_name = 'talent-tech-stack-delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talent'] = TalentProfile.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('talent-dashboard')
