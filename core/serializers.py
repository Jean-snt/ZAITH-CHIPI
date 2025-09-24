from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Message
        fields = ["id", "user", "original_text", "corrected_text", "feedback", "created_at"]
        read_only_fields = ["id", "user", "corrected_text", "feedback", "created_at"]


