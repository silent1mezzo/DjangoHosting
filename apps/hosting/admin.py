from django.contrib import admin
from models import Host, HostType

class HostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class HostTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Host, HostAdmin)
admin.site.register(HostType, HostTypeAdmin)
