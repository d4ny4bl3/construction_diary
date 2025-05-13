from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .serializers import ProjectSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_project(request):
    user = request.user

    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        project = serializer.save(user=user)
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
