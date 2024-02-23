from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CV_Link.common.urls')),
    path('account/', include('CV_Link.account.urls')),
    path('profile/',
         include([
            path('talent/', include('CV_Link.profile_talent.urls')),
            path('recruiter/', include('CV_Link.profile_recruiter.urls')),
            ])),
]


admin.site.site_header = 'CVLink Administrator'
admin.site.site_title = 'CVLink Administrator Page'
admin.site.index_title = 'CVLink Administrator Page'