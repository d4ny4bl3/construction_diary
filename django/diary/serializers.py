from rest_framework import serializers
from .models import Project
from accounts.serializers import UserLightSerializer


class ProjectSerializer(serializers.ModelSerializer):
    user = UserLightSerializer(read_only=True)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"