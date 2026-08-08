from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.conf import settings
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from app_run.enums import UserType
from app_run.models import Run
from app_run.serializers import RunSerializer, UsersSerializer


@api_view(['GET'])
def company_details(request):
    return Response({
        'company_name': f'{settings.COMPANY_NAME}',
        'slogan': f'{settings.SLOGAN}',
        'contacts': f'{settings.CONTACTS}',
    })


class RunViewSet(ModelViewSet):
    queryset = Run.objects.select_related('athlete')
    serializer_class = RunSerializer


class UsersViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        qs = self.queryset
        type_param = self.request.query_params.get('type', None)

        if type_param == UserType.COACH:
            qs_filter = Q(is_staff=True)
        elif type_param == UserType.ATHLETE:
            qs_filter = Q(is_staff=False)
        else:
            qs_filter = Q()

        qs = qs.filter(qs_filter).exclude(is_superuser=True)

        return qs


