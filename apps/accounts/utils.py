import secrets
from django.utils import timezone
from datetime import timedelta

from apps.accounts.models import EmailOTP

def generate_otp():
    return secrets.randbelow(1000000)  # Generates a random number between 0 and 999999

def generate_and_send_otp(user):
    otp = generate_otp()
    expires_at = timezone.now() + timedelta(minutes=10)

    EmailOTP.objects.create(user=user, code=otp, expires_at=expires_at)

    print(f"OTP for {user.email}: {otp}")
    print(f"OTP expires at: {expires_at}")
    return otp