from rest_framework import serializers
from .models import Project, ProjectStatus, Unit, Material, MaterialPurchase, DailyLog
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


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Material
        fields = "__all__"


class MaterialPurchaseSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source="material.name")
    material_unit = serializers.CharField(source="material.unit")

    class Meta:
        model = MaterialPurchase
        fields = "__all__"


class DailyLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyLog
        fields = "__all__"
