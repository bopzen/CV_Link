from django.views import generic
from django.contrib.auth import mixins as auth_mixins

from CV_Link.profile_recruiter.models import RecruiterProfile


class RecruiterDashboardView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    model = RecruiterProfile
    template_name = 'recruiter-profile-dashboard.html'
    context_object_name = 'recruiter_profile'

    def get_object(self, queryset=None):
        return RecruiterProfile.objects.get(user_id=self.request.user)