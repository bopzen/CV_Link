from django.urls import path

from CV_Link.profile_recruiter.views import RecruiterDashboardView, RecruiterEditView, RecruiterAddressEditView, \
    RecruiterAddressCreateView

urlpatterns = [
    path('dashboard/', RecruiterDashboardView.as_view(), name='recruiter-dashboard'),
    path('edit-profile/', RecruiterEditView.as_view(), name='recruiter-edit-profile'),
    path('add-address/<int:pk>/', RecruiterAddressCreateView.as_view(), name='recruiter-create-address'),
    path('edit-address/<int:pk>/', RecruiterAddressEditView.as_view(), name='recruiter-edit-address')
]