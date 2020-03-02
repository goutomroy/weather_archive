from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from apps.archive.models import Archive, Observation, Task
from django.contrib.auth.models import Permission


class PermissionAdmin(admin.ModelAdmin):

    list_display = ['id', 'codename', 'name', 'content_type']
    readonly_fields = ['id']
    list_filter = ['content_type']
    list_display_links = ['id', 'codename']


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


class TaskAdmin(GuardedModelAdmin):

    list_display = ['id', 'title', 'user', 'done']
    readonly_fields = ['id']
    list_display_links = ['id', 'title']


admin.site.register(Permission, PermissionAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Task, TaskAdmin)
