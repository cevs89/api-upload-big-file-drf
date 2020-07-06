from django.contrib.auth.models import User
from upload_file.models import FileUploadCSV


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

    def save(self, request_user, data):
        get_file = data['file_upload']
        get_separator = data['separator']

        try:
            query_user = User.objects.get(pk=request_user)
        except User.DoesNotExist:
            raise ValueError("User Does not exists")

        query_file = FileUploadCSV()
        query_file.user_upload = query_user
        query_file.file_upload = get_file
        query_file.separator = get_separator
        query_file.save()
        return query_file
