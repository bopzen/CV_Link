from django.urls import path

from CV_Link.profile_recruiter.views import RecruiterDashboardView

urlpatterns = [
    path('dashboard/', RecruiterDashboardView.as_view(), name='recruiter-dashboard')
]