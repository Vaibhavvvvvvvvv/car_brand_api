from rest_framework import serializers
from .models import *

class carserilizers(serializers.ModelSerializer):
    class Meta:
        model=Carmodel
        fields='__all__'