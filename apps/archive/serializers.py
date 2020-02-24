from apps.archive.models import Archive
from weather.serializers import DynamicModelSerializer


class ArchiveSerializer(DynamicModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"

    @staticmethod
    def get_upload_fields():
        return 'file',
