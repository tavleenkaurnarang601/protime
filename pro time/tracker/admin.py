from django.contrib import admin
from .models import AuditLog,Company,Project,Task,User
admin.site.register([Company,Project,Task,AuditLog])
@admin.register(User)
class UserAdmin(admin.ModelAdmin): list_display=('email','first_name','role','company','is_active'); list_filter=('role','company','is_active')