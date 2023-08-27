from rest_framework import serializers 
from .models import myAdmin

class adminSerializers(serializers.ModelSerializer):
    class Meta: 
        model = myAdmin
        fields= '__all__'