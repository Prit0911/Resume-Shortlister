from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/', include([
            path('register/', views.RegisterView.as_view(), name='register'),
            path('otp/verify/', views.EmailVerificationView.as_view(), name='otp-verify'),
            path('login/', views.LoginView.as_view(), name='login'),
            path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
            path('logout/', views.LogoutView.as_view(), name='logout'),
            path('change-password/', views.ChangePassowrdView.as_view(), name='change-password'),
            path('password-reset/request/', views.ForgotPasswordView.as_view(), name='password-reset-request'),
            path('password-reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    ])),
    path('users/me/', views.UserProfileView.as_view(), name='profile'),
    path('users/', views.UserListView.as_view(), name='user-list'),
]