from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from datetime import time
from django.core.exceptions import ValidationError

from diary.models import DailyLog, Material, MaterialUsage, Project
from diary.serializers import DailyLogSerializer, MaterialUsageSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_daily_logs(request):
    user = request.user

    daily_logs = DailyLog.objects.filter(project__user=user)
    serializer = DailyLogSerializer(daily_logs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_daily_log(request, daily_log_id):
    user = request.user

    try:
        daily_log = DailyLog.objects.get(id=daily_log_id, project__user=user)
    except DailyLog.DoesNotExist:
        return Response({"error": "Daily log not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DailyLogSerializer(daily_log)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_daily_log(request):
    title = request.data.get("title")
    project_id = request.data.get("project")
    description = request.data.get("description")
    date = request.data.get("date")
    start_time_str = request.data.get("startTime")
    end_time_str = request.data.get("endTime")

    start_time = time.fromisoformat(start_time_str) if start_time_str else None
    end_time = time.fromisoformat(end_time_str) if end_time_str else None

    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    daily_log = DailyLog.objects.create(
        project=project,
        title=title,
        description=description,
        date=date,
        start_time=start_time,
        end_time=end_time
    )

    serializer = DailyLogSerializer(daily_log)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_daily_log(request, daily_log_id):
    user = request.user

    try:
        daily_log = DailyLog.objects.get(id=daily_log_id, project__user=user)
    except DailyLog.DoesNotExist:
        return Response({"error": "Daily log not found"}, status=status.HTTP_404_NOT_FOUND)

    project_id = request.data.get("project")
    title = request.data.get("title")
    description = request.data.get("description")
    date = request.data.get("date")
    start_time_str = request.data.get("startTime")
    end_time_str = request.data.get("endTime")

    start_time = time.fromisoformat(start_time_str) if start_time_str else None
    end_time = time.fromisoformat(end_time_str) if end_time_str else None

    try:
        project = Project.objects.get(id=project_id, user=user)
        daily_log.project = project
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    daily_log.title = title
    daily_log.description = description
    daily_log.date = date
    daily_log.start_time = start_time
    daily_log.end_time = end_time
    daily_log.save()

    return Response(DailyLogSerializer(daily_log).data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_daily_log(request, daily_log_id):
    user = request.user

    try:
        daily_log = DailyLog.objects.get(id=daily_log_id, project__user=user)
    except DailyLog.DoesNotExist:
        return Response({"error": "Daily log not found"}, status=status.HTTP_404_NOT_FOUND)

    daily_log.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_material_usages(request, daily_log_id):
    user = request.user

    usages = (
        MaterialUsage.objects
        .filter(daily_log=daily_log_id, material__user=user)
        .select_related("material", "material__unit")
    )
    serializer = MaterialUsageSerializer(usages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_material_usage(request, daily_log_id, usage_id):
    user = request.user

    try:
        usage = MaterialUsage.objects.get(id=usage_id, daily_log=daily_log_id, material__user=user)
    except MaterialUsage.DoesNotExist:
        return Response({"error": "Material usage not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaterialUsageSerializer(usage)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_material_usage(request, daily_log_id):
    user = request.user

    material_id = request.data.get("material")
    used_quantity = request.data.get("used_quantity")
    used_at = request.data.get("used_at")

    try:
        daily_log = DailyLog.objects.get(id=daily_log_id, project__user=user)
        material = Material.objects.get(id=material_id, user=user)

        material_usage = MaterialUsage(
            daily_log=daily_log,
            material=material,
            used_quantity=used_quantity,
            used_at=used_at
        )
        material_usage.save()

    except ValidationError as e:
        return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)
    except DailyLog.DoesNotExist:
        return Response({"error": "Daily log not found"}, status=status.HTTP_404_NOT_FOUND)
    except Material.DoesNotExist:
        return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaterialUsageSerializer(material_usage)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_material_usage(request, daily_log_id, usage_id):
    pass


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_material_usage(request, daily_log_id, usage_id):
    user = request.user

    try:
        usage = MaterialUsage.objects.get(id=usage_id, daily_log=daily_log_id, material__user=user)
    except MaterialUsage.DoesNotExist:
        return Response({"error": "Material usage not found"}, status=status.HTTP_404_NOT_FOUND)

    usage.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
