from django.urls import path, include
from CV_Link.account.views import AccountRegisterView, AccountLoginView, AccountLogoutView, AccountLogoutPageView, \
    AccountDeleteView, AccountPasswordChangeView, AccountPasswordChangeConfirmView

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register-page'),
    path('login/', AccountLoginView.as_view(), name='login-page'),
    path('logout/',
         include([
            path('', AccountLogoutPageView.as_view(), name='logout-page'),
            path('confirm', AccountLogoutView.as_view(), name='logout-confirmation-page'),
            ])),
    path('delete/', AccountDeleteView.as_view(), name='delete-page'),
    path('change-password/',
         include([
            path('', AccountPasswordChangeView.as_view(), name='change-password-page'),
            path('confirm', AccountPasswordChangeConfirmView.as_view(), name='change-password-confirmation-page'),
            ])),
    ]
