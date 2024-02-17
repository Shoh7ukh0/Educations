from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone_number', )

class CustomPasswordResetSerializer(serializers.Serializer):
    # Add any additional fields you need for password reset
    custom_field = serializers.CharField(max_length=255, required=False)

    def validate_custom_field(self, value):
        # You can add custom validation logic for the new field here
        # For example, check if the value meets certain criteria
        return value