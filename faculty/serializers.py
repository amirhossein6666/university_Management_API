from rest_framework import serializers
from .models import faculty

class facultySerializers(serializers.ModelSerializer): 
    class Meta: 
        model = faculty
        fields= '__all__'