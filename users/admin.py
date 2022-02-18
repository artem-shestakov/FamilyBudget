from csv import list_dialects
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdministrator
from django.utils.translation import gettext, gettext_lazy as _

from .models import Family
from .forms import NewUserChangeForm


User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdministrator):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
    search_fields = ('first_name', 'last_name', 'email')
    form = NewUserChangeForm


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass