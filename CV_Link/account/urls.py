from django.urls import path, include
from CV_Link.account.views import AccountRegisterView, AccountLoginView, AccountLogoutView, AccountLogoutPageView, \
    AccountDeleteView

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register-page'),
    path('login/', AccountLoginView.as_view(), name='login-page'),
    path('logout/', include([
        path('', AccountLogoutPageView.as_view(), name='logout-page'),
        path('confirm', AccountLogoutView.as_view(), name='logout-confirmation'),
    ])),
    path('delete/', AccountDeleteView.as_view(), name='delete-page')
]