from django.urls import path

from CV_Link.profile_talent.views import TalentDashboardView, TalentEditView, TalentEducationCreateView, \
    TalentEducationEditView, TalentEducationDeleteView

urlpatterns = [
    path('dashboard/', TalentDashboardView.as_view(), name='talent-dashboard'),
    path('edit-profile/', TalentEditView.as_view(), name='talent-edit-profile'),
    path('add-education/<int:pk>/', TalentEducationCreateView.as_view(), name='talent-create-education'),
    path('edit-education/<int:pk>/', TalentEducationEditView.as_view(), name='talent-edit-education'),
    path('delete-education/<int:pk>/', TalentEducationDeleteView.as_view(), name='talent-delete-education'),
]