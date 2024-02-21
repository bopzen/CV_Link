from django.contrib import admin

from CV_Link.profile_talent.models import TalentProfile, Education, WorkExperience


@admin.register(TalentProfile)
class AdminTalentProfile(admin.ModelAdmin):
    pass


@admin.register(Education)
class AdminEducation(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class AdminWorkExperience(admin.ModelAdmin):
    pass