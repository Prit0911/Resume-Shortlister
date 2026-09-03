from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('otp/verify/', views.EmailVerificationView.as_view(), name='otp_verify'),
]