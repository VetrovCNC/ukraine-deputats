from rest_framework import serializers
from deputats.models import Deputat


class DeputatSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Deputat
        fields = (
            'id',
            'surname',
            'name',
            'patronymic',
            'selected_by',
            'party',
            'party_number',
            'fraction',
            'position',
            'region',
            'gender',
        )