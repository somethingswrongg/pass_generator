from django.contrib import admin
from .models import Passwords


class PasswordsAdmin(admin.ModelAdmin):
    list_display = 'user', 'password', 'created_at'


admin.site.register(Passwords, PasswordsAdmin)
