from django.views import generic


class TalentDashboardPageView(generic.TemplateView):
    template_name = 'talent-profile-dashboard.html'