from rest_framework import serializers
from .models import professor

class professorSerializer(serializers.ModelSerializer):
    class Meta:
        model = professor
        fields = ['username' , 'password' , 'faculty' , 'students', 'id']