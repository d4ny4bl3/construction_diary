from rest_framework import serializers
from .models import Project, ProjectStatus
from accounts.serializers import UserLightSerializer


class ProjectStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectStatus
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    user = UserLightSerializer(read_only=True)
    status_name = serializers.CharField(source="status.name", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"