import serpy
from datetime import datetime


class UploadFileSerializer(serpy.Serializer):
    id = serpy.Field()
    file_upload = serpy.MethodField()
    user_upload = serpy.MethodField()
    pub_date = serpy.MethodField()

    def get_file_upload(self, obj):
        if obj.file_upload is not None:
            return obj.file_upload.url

    def get_user_upload(self, obj):
        if obj.user_upload is not None:
            return obj.user_upload.username

    def get_pub_date(self, obj):
        if obj.pub_date is not None:
            return datetime.strftime(obj.pub_date, "%Y-%m-%d %H:%M")
