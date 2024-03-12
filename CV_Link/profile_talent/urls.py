from django.urls import path

from CV_Link.profile_talent.views import TalentDashboardView, TalentEditView, TalentEducationCreateView, \
    TalentEducationEditView, TalentEducationDeleteView, TalentWorkExperienceCreateView, TalentWorkExperienceEditView, \
    TalentWorkExperienceDeleteView, TalentTechStackCreateView, TalentTechStackEditView, TalentTechStackDeleteView, \
    TalentContactsCreateView, TalentContactsEditView

urlpatterns = [
    path('dashboard/', TalentDashboardView.as_view(), name='talent-dashboard'),
    path('edit-profile/', TalentEditView.as_view(), name='talent-edit-profile'),
    path('add-education/<int:pk>/', TalentEducationCreateView.as_view(), name='talent-create-education'),
    path('edit-education/<int:pk>/', TalentEducationEditView.as_view(), name='talent-edit-education'),
    path('delete-education/<int:pk>/', TalentEducationDeleteView.as_view(), name='talent-delete-education'),
    path('add-work-experience/<int:pk>/', TalentWorkExperienceCreateView.as_view(), name='talent-create-work-experience'),
    path('edit-work-experience/<int:pk>/', TalentWorkExperienceEditView.as_view(), name='talent-edit-work-experience'),
    path('delete-work-experience/<int:pk>/', TalentWorkExperienceDeleteView.as_view(), name='talent-delete-work-experience'),
    path('add-tech-stack/', TalentTechStackCreateView.as_view(), name='talent-create-tech-stack'),
    path('edit-tech-stack/<int:pk>/', TalentTechStackEditView.as_view(), name='talent-edit-tech-stack'),
    path('delete-tech-stack/<int:pk>/', TalentTechStackDeleteView.as_view(), name='talent-delete-tech-stack'),
    path('add-contacts/', TalentContactsCreateView.as_view(), name='talent-create-contacts'),
    path('edit-contacts/<int:pk>/', TalentContactsEditView.as_view(), name='talent-edit-contacts'),
]