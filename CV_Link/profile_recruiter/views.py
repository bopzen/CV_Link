from django.views import generic


class RecruiterDashboardPageView(generic.TemplateView):
    template_name = 'recruiter-profile-dashboard.html'