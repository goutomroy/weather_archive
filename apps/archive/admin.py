from django.contrib import admin
from apps.archive.models import Archive, Observation


class ArchiveAdmin(admin.ModelAdmin):

    list_display = ['id', 'status', 'created', 'file']
    readonly_fields = ['id', 'created']
    list_display_links = ['id', 'status']
    ordering = ['-created']


class ObservationAdmin(admin.ModelAdmin):

    list_display = ['id', 'date', 'temperature', 'rainfall']
    readonly_fields = ['id', 'date']
    list_display_links = ['id', 'date']
    ordering = ['-date']


admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Observation, ObservationAdmin)
