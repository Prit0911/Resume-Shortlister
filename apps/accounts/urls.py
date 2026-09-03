from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include([
            path('register/', views.RegisterView.as_view(), name='register'),
            path('otp/verify/', views.EmailVerificationView.as_view(), name='otp_verify'),
            path('login/', views.LoginView.as_view(), name='login'),
    ])),
]