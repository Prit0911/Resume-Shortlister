from rest_framework import serializers
from .models import Skill

class SkillsListSerializer(serializers.ModelSerializer):
     class Meta:
            model = Skill
            fields = ['id', 'name', 'slug', 'is_active']
            read_only_fields = fields