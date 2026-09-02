from django.contrib import admin
from .models import User, EmailOTP
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    model = User

    ordering = ('email',)
    list_display = ('email', 'username', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    readonly_fields = ('last_login', 'date_joined', 'created_at', 'updated_at', 'id')

admin.site.register(User, UserAdmin)

@admin.register(EmailOTP)
class EmailOTPAdmin(admin.ModelAdmin):
    model = EmailOTP

    ordering = ('user',)
    list_display = ('user', 'code', 'is_used', 'expires_at')
    list_filter = ('is_used',)
    search_fields = ('user__email', 'code')

    fieldsets = (
        (None, {'fields': ('user', 'code')}),
        ('Status', {'fields': ('is_used',)}),
        ('Expiration', {'fields': ('expires_at',)}),
    )

    readonly_fields = ('created_at', 'updated_at', 'id')