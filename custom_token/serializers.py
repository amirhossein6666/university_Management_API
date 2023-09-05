from rest_framework import serializers
from .models import AdminCustomToken, ProfessorCustomToken, StudentCustomToken
class adminTokenSerializers(serializers.ModelSerializer):
    class Meta:
        model= AdminCustomToken
        fields = ['user', 'key']

class professorTokenSerializers(serializers.ModelSerializer):
    class Meta:
        model= ProfessorCustomToken
        fields = ['user', 'key']

class studentTokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentCustomToken
        fields = ['user', 'key']
