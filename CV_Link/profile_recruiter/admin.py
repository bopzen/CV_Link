from django.contrib import admin

from CV_Link.profile_recruiter.models import RecruiterProfile, Address, Contacts


@admin.register(RecruiterProfile)
class AdminRecruiter(admin.ModelAdmin):
    pass


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class AdminContacts(admin.ModelAdmin):
    pass
