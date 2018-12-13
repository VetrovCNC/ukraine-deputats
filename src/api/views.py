from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import DeputatSerializer
from deputats.models import Deputat


@permission_classes((IsAuthenticated, ))
class DeputatViewSet(viewsets.ModelViewSet):

    queryset = Deputat.objects.all()
    serializer_class = DeputatSerializer