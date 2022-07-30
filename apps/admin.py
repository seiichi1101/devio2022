from django.contrib import admin

from apps.models import Organization, RoleGroup

# Register your models here.
admin.site.register(RoleGroup)
admin.site.register(Organization)
