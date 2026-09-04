from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import (
    RegisterSerializer, 
    EmailVerificationSerializer, 
    LoginSerializer, 
    LogoutSerializer, 
    ChangePasswordSerializer, 
    ForgotPasswordRequestSerializer,
    PasswordResetConfirmSerializer,
    UserProfileSerializer,
)

from .utils import generate_and_send_otp, get_tokens_for_user

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated

from .models import EmailOTP, User

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            generate_and_send_otp(user)
            return Response(
                {"message": "User registered successfully. Please check your email for the OTP to activate your account."}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailVerificationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            otp = serializer.validated_data['code']

            otp.is_used = True
            otp.save()

            user.is_active=True
            user.save()

            tokens = get_tokens_for_user(user)

            return Response(
                {
                    "message": "Email verified successfully.",
                    "tokens": tokens,
                },
                status = status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']

            tokens = get_tokens_for_user(user)

            return Response(
                {
                    "message": "Logged in successfully",
                    "tokens": tokens,
                },
                status = status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token = RefreshToken(serializer.validated_data['token'])
            token.blacklist()
        except TokenError:
            return Response({"error":"Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class ChangePassowrdView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()

            return Response({
                "message": "Password changed successfully!"
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordRequestSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.get(email=serializer.validated_data['email'])
            generate_and_send_otp(user)

            return Response({
                "message": "OTP sent to your email."
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            otp = serializer.validated_data['code']

            otp.is_used = True
            otp.save()

            user.set_password(serializer.validated_data['password'])
            user.save()

            return Response({
                "message": "Password reset successful. Please log in with your new password"
            }, status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)