from apps.archive.models import Archive, Observation
from weather.serializers import DynamicModelSerializer


class ObservationSerializer(DynamicModelSerializer):
    class Meta:
        model = Observation
        fields = "__all__"


class ArchiveSerializer(DynamicModelSerializer):
    class Meta:
        model = Archive
        # fields = "__all__"
        exclude = ['observations']

    @staticmethod
    def get_upload_fields():
        return 'file',
