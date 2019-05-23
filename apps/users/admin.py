from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group as BaseGroup
from registration.models import RegistrationProfile as BaseRegistrationProfile

from apps.users.models import Group, RegistrationProfile, User


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ['id']
    list_display = (
        'id',
        'email',
        'is_active',
        'is_superuser',
        'last_login',
        'date_joined',
    )
    list_display_links = ('id', 'email')
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
        'date_joined'
    )
    search_fields = ('email', )

    fieldsets = (
        (None, {
            'fields': ('password', )}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        ('Authentication', {
            'fields': ('email', 'password1', 'password2'),
        })
    )

    class RegistrationProfileInline(admin.TabularInline):
        model = RegistrationProfile
        extra = 0

    inlines = [RegistrationProfileInline,]



admin.site.unregister(BaseGroup)
admin.site.unregister(BaseRegistrationProfile)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


@admin.register(RegistrationProfile)
class RegistrationProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'activated')
    list_display_links = ('id', 'user')
    list_filter = ('activated', )
