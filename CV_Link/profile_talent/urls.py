from django.urls import path

from CV_Link.profile_talent.views import TalentDashboardView

urlpatterns = [
    path('dashboard/', TalentDashboardView.as_view(), name='talent-dashboard')
]