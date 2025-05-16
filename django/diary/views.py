from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Project, ProjectStatus
from .serializers import ProjectSerializer, ProjectStatusSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_project(request):
    user = request.user

    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        project = serializer.save(user=user)
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_project(request, project_id, slug):
    user = request.user

    try:
        project = Project.objects.get(id=project_id, user=user, slug=slug)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(project, data=request.data, partial=True)
    if serializer.is_valid():
        project = serializer.save()
        return Response(ProjectSerializer(project).data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_projects(request):
    user = request.user
    projects = Project.objects.filter(user=user).order_by("-id")

    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_project(request, project_id, slug):
    user = request.user

    try:
        project = Project.objects.get(id=project_id, user=user, slug=slug)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_statuses(request):
    user = request.user
    project_status = ProjectStatus.objects.filter(user=user)

    serializer = ProjectStatusSerializer(project_status, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
