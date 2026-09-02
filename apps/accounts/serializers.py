from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=15)
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=150)

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        
        if len(value)<10:
            raise serializers.ValidationError("Phone number must contain 10 digits")
        return value


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")

        if User.objects.filter(email=data['email'], is_active=True).exists():
            raise serializers.ValidationError("Email is already in use.")

        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError({"username": "Username already in use"})
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        email = validated_data["email"]

        existing_user = User.objects.filter(email=email, is_active=False).first()
        if existing_user:
            for field, value in validated_data.items():
                setattr(existing_user, field, value)

            existing_user.set_password(password)
            existing_user.save()
            return existing_user

        user = User.objects.create_user(password=password, **validated_data)
        user.is_active = False
        user.save()
        return user

