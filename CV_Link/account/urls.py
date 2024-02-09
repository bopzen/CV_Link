from django.urls import path
from CV_Link.account.views import AccountRegisterView, AccountLoginView, AccountLogoutView

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register-page'),
    path('login/', AccountLoginView.as_view(), name='login-page'),
    path('logout/', AccountLogoutView.as_view(), name='logout-page'),
]