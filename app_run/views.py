from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework.viewsets import ModelViewSet

from app_run.models import Run
from app_run.serializers import RunSerializer


@api_view(['GET'])
def company_details(request):
    return Response({
        'company_name': f'{settings.COMPANY_NAME}',
        'slogan': f'{settings.SLOGAN}',
        'contacts': f'{settings.CONTACTS}',
    })


class RunViewSet(ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
