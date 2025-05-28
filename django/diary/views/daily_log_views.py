from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from datetime import time

from diary.models import DailyLog, Project
from diary.serializers import DailyLogSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_daily_logs(request):
    user = request.user

    daily_logs = DailyLog.objects.filter(project__user=user)
    serializer = DailyLogSerializer(daily_logs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_daily_log(request, daily_id):
    user = request.user

    try:
        daily_log = DailyLog.objects.get(id=daily_id, project__user=user)
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
