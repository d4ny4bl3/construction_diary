from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from diary.models import Unit, Material
from diary.serializers import UnitSerializer, MaterialSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_units(request):
    user = request.user

    units = Unit.objects.filter(user=user).order_by("id")
    serializer = UnitSerializer(units, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_material(request):
    user = request.user

    try:
        unit_id = request.data.get("unit")
        unit = Unit.objects.get(id=unit_id, user=user)

        material = Material.objects.create(
            user=user,
            name=request.data.get("name"),
            unit=unit
        )

        serializer = MaterialSerializer(material)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Unit.DoesNotExist:
        return Response({"error": "Unit not found"}, status=status.HTTP_400_BAD_REQUEST)