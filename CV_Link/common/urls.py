from django.urls import path

from CV_Link.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
]