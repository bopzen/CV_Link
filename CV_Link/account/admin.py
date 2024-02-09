from django.contrib import admin
from CV_Link.account.models import AccountUser


@admin.register(AccountUser)
class AdminAccountUser(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'password',
        'account_type',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',
    ]

    fieldsets = (
        ('User Info', {
            'fields': ('username', 'email', 'password', 'account_type'),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.set_password(form.cleaned_data['password'])
        elif form.cleaned_data['password'] != self.model.objects.get(pk=obj.pk).password:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)




