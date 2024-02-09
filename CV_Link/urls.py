from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CV_Link.common.urls')),
    path('account/', include('CV_Link.account.urls')),
]
