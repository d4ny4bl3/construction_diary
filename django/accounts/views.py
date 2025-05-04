from accounts.serializers import UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
        return Response({"error": "User doesn`t exits"}, status=status.HTTP_401_UNAUTHORIZED)

    user = authenticate(request, username=user_obj.username, password=password)

    if user is not None:
        login(request, user)
        user_data = UserSerializer(user).data
        return Response({"user": user_data}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid login"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
