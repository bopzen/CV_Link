from django.urls import path

from CV_Link.profile_recruiter.views import RecruiterDashboardPageView

urlpatterns = [
    path('dashboard/', RecruiterDashboardPageView.as_view(), name='recruiter-dashboard')
]