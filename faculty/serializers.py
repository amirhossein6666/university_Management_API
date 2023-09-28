from rest_framework import serializers
from .models import faculty

class facultySerializers(serializers.ModelSerializer): 
    class Meta: 
        model = faculty
        fields= ['name', 'courses', 'id']