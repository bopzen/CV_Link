from django.views import generic

from CV_Link.profile_talent.models import TalentProfile


class TalentDashboardView(generic.TemplateView):
    model = TalentProfile
    template_name = 'talent-profile-dashboard.html'
    context_object_name = 'talent_profile'

    def get_object(self, queryset=None):
        return TalentProfile.objects.get(user_id=self.request.user)