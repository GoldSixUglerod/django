import logging

from rest_framework import mixins, viewsets

from api.serializers.EmployeeSerializer import EmployeeReadSerializer
from api.models.Employee import Employee

logger = logging.getLogger(__name__)


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    """This ViewSet processes all requests with UserDocumentImage"""

    SERIALIZER_MAP = {  # we need different serializer depending on action
        "retrieve": EmployeeReadSerializer,
    }

    def get_queryset(self):
        queryset = Employee.objects.all()
        pk = self.request.query_params.get('pk')
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        return queryset

    def get_serializer_class(self):
        return self.SERIALIZER_MAP[self.action]
