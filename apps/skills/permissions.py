from rest_framework.permissions import BasePermission

class IsRecruiter(BasePermission):
    message = "Only Recruiters can perform this action."

    def has_permission(self, request, view):
        user = request.user
        return bool(
            user and
            user.is_authenticated and
            getattr(user, 'role', None) == 'recruiter'
        )