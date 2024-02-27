from django.urls import path

from CV_Link.profile_recruiter.views import RecruiterDashboardView, RecruiterEditView, RecruiterAddressEditView, \
    RecruiterAddressCreateView, RecruiterContactsCreateView, RecruiterContactsEditView

urlpatterns = [
    path('dashboard/', RecruiterDashboardView.as_view(), name='recruiter-dashboard'),
    path('edit-profile/', RecruiterEditView.as_view(), name='recruiter-edit-profile'),
    path('add-address/<int:pk>/', RecruiterAddressCreateView.as_view(), name='recruiter-create-address'),
    path('edit-address/<int:pk>/', RecruiterAddressEditView.as_view(), name='recruiter-edit-address'),
    path('add-contacts/<int:pk>/', RecruiterContactsCreateView.as_view(), name='recruiter-create-contacts'),
    path('edit-contacts/<int:pk>', RecruiterContactsEditView.as_view(), name='recruiter-edit-contacts'),
]