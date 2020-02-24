from django.contrib import admin
from apps.archive.models import Archive


class ArchiveAdmin(admin.ModelAdmin):

    list_display = ['id', 'status', 'created', 'file']
    readonly_fields = ['id', 'created']
    list_display_links = ['id', 'status']
    ordering = ['-created']


admin.site.register(Archive, ArchiveAdmin)
