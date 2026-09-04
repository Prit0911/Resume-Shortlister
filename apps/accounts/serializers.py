from rest_framework import serializers
from .models import User, EmailOTP
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from django.contrib.auth import authenticate

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

class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data['email']
        code = data['code']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        otp = EmailOTP.objects.filter(user=user, code=code, is_used=False, expires_at__gt=timezone.now()).first()

        if otp is None:
            raise serializers.ValidationError("Invalid or expired OTP.")

        if otp.expires_at < timezone.now():
            raise serializers.ValidationError("OTP has expired.")

        if otp.code != code:
            raise serializers.ValidationError("Invalid OTP.")

        data['user'] = user
        data['code'] = otp

        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']

        user = authenticate(email=email, password=password)

        if user is None:
            existing_user = User.objects.filter(email=email).first()

            if existing_user and not existing_user.is_active and existing_user.check_password(password):
                raise serializers.ValidationError(
                    "Your account is not verified. Please verify your email before logged in."
                )

            raise serializers.ValidationError("Invalid email or password")

        data["user"]=user
        return data     

class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField()