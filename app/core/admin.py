from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

# this hook is needed to make django projects translatable,
# Wrap the texts with this if you want django to automatically translate -> Example: _('Translate this text')
from django.utils.translation import gettext as _

# This class is used just for the admin interface.
# Nothing changes except the way admin page looks
class UserAdmin(BaseUserAdmin):
    # Order the list by *id*
    ordering = ['id']

    # Fields to be included in list users page
    list_display = ['email', 'name']

    # Fields to be included on change user page (edit page)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    # Fields to be included on add page
    add_fieldsets = (
        # None - First field -> title of the section
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
