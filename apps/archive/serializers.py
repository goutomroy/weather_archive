from django.contrib.auth.models import User
from apps.archive.models import Archive, Observation, Task
from weather.serializers import DynamicModelSerializer


class ObservationSerializer(DynamicModelSerializer):
    class Meta:
        model = Observation
        fields = "__all__"


class ArchiveSerializer(DynamicModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"


class UserSerializer(DynamicModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    @staticmethod
    def get_nested_fields():
        return 'id', 'username'


class TaskSerializer(DynamicModelSerializer):
    user = UserSerializer(fields=UserSerializer.get_nested_fields())

    class Meta:
        model = Task
        fields = "__all__"


