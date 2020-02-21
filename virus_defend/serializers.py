from rest_framework import serializers
from . import models

class HealthstateSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Healthstate
        fields="__all__"