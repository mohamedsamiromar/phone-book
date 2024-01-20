from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin( BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        (('Personal info'), {
            'fields': ('first_name', 'last_name', 'preferred_lang', 'is_email_verified', 'email_verification_token')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_blocked',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'email', 'first_name',
                    'last_name', 'is_staff', 'get_user_groups']
    search_fields = ('username', 'email', 'first_name', 'last_name')
    djangoql_completion_enabled_by_default = False
    ordering = ('email',)

    def get_user_groups(self, obj):
        groups = []
        for group in obj.groups.all():
            groups.append(group.name)

        return ', '.join(groups)

    get_user_groups.short_description = 'Groups'