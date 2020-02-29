from guardian.shortcuts import assign_perm
from rest_framework import fields, serializers
from apps.archive.models import Archive, Observation, Task


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = "__all__"


class ArchiveSerializer(serializers.ModelSerializer):
    status = fields.IntegerField(read_only=True)

    class Meta:
        model = Archive
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        task = super().create(validated_data)
        assign_perm('change_delete_task', task.user, task)
        return task


