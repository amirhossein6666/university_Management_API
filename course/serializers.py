from rest_framework import serializers
from .models import course

class courseSerializers(serializers.ModelSerializer):
    class Meta:
        model = course    
        fields = '__all__'