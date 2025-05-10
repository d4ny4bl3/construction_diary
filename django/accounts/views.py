from accounts.serializers import UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(["POST"])
def login_view(request):
    if request.user.is_authenticated:
        user_data = UserSerializer(request.user).data
        return Response({"user": user_data}, status=status.HTTP_200_OK)

    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Missing username or password"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_obj = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "User doesn`t exist"}, status=status.HTTP_401_UNAUTHORIZED)

    user = authenticate(request, username=user_obj.username, password=password)

    if user is not None:
        login(request, user)
        user_data = UserSerializer(user).data
        return Response({"user": user_data}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid login"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user_data = UserSerializer(request.user)
    return Response(user_data.data)
