from django.urls import path

from CV_Link.profile_talent.views import TalentDashboardPageView

urlpatterns = [
    path('dashboard/', TalentDashboardPageView.as_view(), name='talent-dashboard')
]