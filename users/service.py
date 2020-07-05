from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserService:

    def save(self, data, request_user):
        try:
            query_user = User.objects.get(pk=request_user)
        except User.DoesNotExist:
            raise ValueError("User Does not exists")

        if 'first_name' in data or 'last_name' in data or 'email' in data:
            if 'first_name' in data:
                query_user.first_name = data['first_name']

            if 'last_name' in data:
                query_user.last_name = data['last_name']

            if 'email' in data:
                query_user.email = data['email']
            query_user.save()
        else:
            raise ValueError("you need to send one of the following fields: [first_name, last_name, email]")

        return query_user

    def list(self, request_user):
        try:
            query_user = User.objects.get(pk=request_user)
        except User.DoesNotExist:
            raise ValueError("User Does not exists")

        return query_user

    def change_password(self, data, request_user):
        try:
            query_user = User.objects.get(pk=request_user)
        except User.DoesNotExist:
            raise ValueError("User Does not exists")

        try:
            validate_password(data['password'])
        except Exception as error:
            raise ValueError(error)

        if data['password'] == data['password_confirm']:
            query_user.set_password(data['password'])
            query_user.save()
        else:
            raise ValueError("Passwords must be the same")

        return query_user
