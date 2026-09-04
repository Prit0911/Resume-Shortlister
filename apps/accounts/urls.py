from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/', include([
            path('register/', views.RegisterView.as_view(), name='register'),
            path('otp/verify/', views.EmailVerificationView.as_view(), name='otp_verify'),
            path('login/', views.LoginView.as_view(), name='login'),
            path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
            path('logout/', views.LogoutView.as_view(), name='logout'),
    ])),
]