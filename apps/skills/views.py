from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Skill
from .permissions import IsRecruiter

from .serializers import (
    SkillsListSerializer,  
    SkillsCreateSerializer, 
)

class SkillsView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsRecruiter()]
        return [IsAuthenticated]

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillsListSerializer(
            skills, 
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkillsCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)

        return Response(
            SkillsCreateSerializer(serializer.instance).data,
            status=status.HTTP_201_CREATED
        )