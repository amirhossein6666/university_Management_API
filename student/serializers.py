from rest_framework import serializers
from .models import student

class studentSerializers(serializers.ModelSerializer):
    class Meta: 
        model = student
        fields = ['username', 'grades', 'professors', 'courses']