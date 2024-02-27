from django.urls import path

from CV_Link.profile_talent.views import TalentDashboardView, TalentEditView

urlpatterns = [
    path('dashboard/', TalentDashboardView.as_view(), name='talent-dashboard'),
    path('edit-profile/', TalentEditView.as_view(), name='talent-edit-profile'),

]