from rest_framework import serializers
from .models import customUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ['username', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = customUser(
            username=validated_data['username'],
            role=validated_data['role'],
            password=validated_data['password'],
        )
        
        user.save()
        return user