from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from users.validators import (
    ValidateObtaineToken, UserProfileValidator, ValidateChangePassword)
from users.service import UserService
from users.serializers import UserProfileSerializer, UserAutentication


class ObtainTokenCustom(ObtainAuthToken):
    def post(self, request):
        get_validation = ValidateObtaineToken(request.data)

        if get_validation.validate():
            serializer = self.serializer_class(data=request.data)

            data = serializer.initial_data
            user_name = data['username']

            try:
                User.objects.get(username=user_name)
            except User.DoesNotExist:
                return Response(
                    {'message': 'Username does not exist'},
                    status=status.HTTP_400_BAD_REQUEST
                    )

            if serializer.is_valid():
                token, created = Token.objects.get_or_create(
                        user=serializer.validated_data['user']
                    )

                # Write soem logic code here
                serializer = UserAutentication(token)
                return Response(
                        serializer.data, status=status.HTTP_200_OK
                    )
            return Response(
                {'message': 'Incorrect username or password, please check'},
                status=status.HTTP_400_BAD_REQUEST
             )
        else:
            return Response(get_validation.errors())


class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    queryset = User.objects.filter()
    service_user = UserService()

    def list(self, request):
        try:
            data_user = self.service_user.list(request.user.id)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data_user)
        return Response(
                serializer.data, status=status.HTTP_200_OK
            )

    def update(self, request, pk=None):
        get_validation = UserProfileValidator(request.data)

        if get_validation.validate():
            get_data = get_validation.data

            try:
                id_user = int(pk)
            except Exception as e:
                return Response(
                        {'message': "It is not integer", 'detail': str(e)},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            try:
                data_user = self.service_user.save(get_data, id_user)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data_user)
            return Response(
                    serializer.data, status=status.HTTP_200_OK
                )
        else:
            return Response(get_validation.errors())

    def change_password(self, request, pk=None):
        get_validation = ValidateChangePassword(request.data)

        if get_validation.validate():
            get_data = get_validation.data

            try:
                id_user = int(pk)
            except Exception as e:
                return Response(
                        {'message': "It is not integer", 'detail': str(e)},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            try:
                data_user = self.service_user.change_password(get_data, id_user)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data_user)
            return Response(
                    serializer.data, status=status.HTTP_200_OK
                )
        else:
            return Response(get_validation.errors())
