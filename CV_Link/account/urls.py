from django.urls import path
from CV_Link.account.views import AccountRegisterView

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register-page'),
]