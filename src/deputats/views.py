from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Deputat
from api.serializers import DeputatSerializer


class DeputatList(ListAPIView):
    queryset = Deputat.objects.all()
    serializer_class = DeputatSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        surname = self.kwargs.get('surname')
        if surname:
            return qs.filter(surname=surname)
        return qs


@permission_classes((IsAuthenticated, ))
class DeputatRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Deputat.objects.all()
    serializer_class = DeputatSerializer
    lookup_field = 'id'
