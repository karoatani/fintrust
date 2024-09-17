from rest_framework import serializers
from .models import Account

class SignupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(max_length=255, required=True)
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "email", "password"]