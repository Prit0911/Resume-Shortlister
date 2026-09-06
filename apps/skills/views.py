from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Skill

from .serializers import (
    SkillsListSerializer,   
)

class SkillsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillsListSerializer(
            skills, 
            many=True
        )

        return Response(serializer.data, status=status.HTTP_200_OK)