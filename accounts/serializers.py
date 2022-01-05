from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser

        fields =["email", "username", "password"]

    def validate(self, attrs):   
        email=attrs.get('email', "") 
        username=attrs.get('username', "")

        if not username.isalnum():
            raise serializers.ValidationError("The username must be alphanumeric")
        return attrs    

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
        
