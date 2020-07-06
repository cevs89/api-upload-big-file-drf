from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FileUploadParser


from upload_file.models import FileUploadCSV
from upload_file.validators import ValidateUploadFile
from upload_file.serializers import UploadFileSerializer
from upload_file.service import UploadFileService
from upload_file.save_transactions import SaveClientTransactions


class ResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class ListModelMixin(object):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UploadFileViewSet(ListModelMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadFileSerializer
    queryset = FileUploadCSV.objects.filter()
    pagination_class = ResultsSetPagination
    parser_class = (FileUploadParser,)

    service_file = UploadFileService()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user_upload__username', 'id', 'file_upload', 'pub_date']
    ordering_fields = "__all__"

    def get(self, request):
        try:
            date_file = self.service_file.list(request.user.id)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(date_file, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            id_user = int(pk)
        except Exception as e:
            return Response(
                    {'message': "It is not integer", 'detail': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        try:
            date_file = self.service_file.details(request.user.id, id_user)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(date_file)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        get_validation = ValidateUploadFile()

        try:
            file_validate = get_validation.file(request.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        try:
            date_file = self.service_file.save(
                request.user.id, request.data, file_validate)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        # Save file, external DB
        """
        Este proceso deberia ser una tarea en segun plano manejado con Celery
        """
        service_transactions = SaveClientTransactions()
        try:
            service_transactions.process_item(date_file)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(date_file)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
