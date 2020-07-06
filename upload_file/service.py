from django.contrib.auth.models import User
from upload_file.models import FileUploadCSV
from django.core.files.base import ContentFile


class UploadFileService:

    def list(self, request_user):
        try:
            query_user = User.objects.get(pk=request_user)
        except User.DoesNotExist:
            raise ValueError("User Does not exists")

        query_file = FileUploadCSV.objects.filter(user_upload=query_user)
        if query_file.exists():
            return query_file
        else:
            raise ValueError(
                "User {}, no files available".format(query_user.username))

    def details(self, request_user, data):
        try:
            query_user = User.objects.get(pk=request_user)
        except User.DoesNotExist:
            raise ValueError("User Does not exists")

        try:
            query_file = FileUploadCSV.objects.get(
                pk=data, user_upload=query_user)
        except FileUploadCSV.DoesNotExist:
            raise ValueError("UploadFile Does not exists")

        return query_file

    def save(self, request_user, data, df):
        get_separator = data['separator']

        try:
            query_user = User.objects.get(pk=request_user)
        except User.DoesNotExist:
            raise ValueError("User Does not exists")

        file_save = ContentFile(str(df), 'file_save.csv')
        try:
            query_file = FileUploadCSV()
            query_file.user_upload = query_user
            query_file.file_upload = file_save
            query_file.separator = get_separator
            query_file.save()
        except Exception as e:
            raise ValueError(str(e))

        return query_file
