from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from diary.models import Unit, Material, MaterialPurchase
from diary.serializers import UnitSerializer, MaterialSerializer, MaterialPurchaseSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_units(request):
    user = request.user

    units = Unit.objects.filter(user=user).order_by("id")
    serializer = UnitSerializer(units, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_materials(request):
    user = request.user

    materials = Material.objects.filter(user=user)
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_material(request, material_id):
    user = request.user

    try:
        material = Material.objects.get(id=material_id, user=user)
    except Material.DoesNotExist:
        return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaterialSerializer(material)
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


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_material(request, material_id):
    user = request.user

    try:
        material = Material.objects.get(id=material_id, user=user)
    except Material.DoesNotExist:
        return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)

    name = request.data.get("name")
    unit_id = request.data.get("unit")

    if name:
        material.name = name

    if unit_id:
        try:
            unit = Unit.objects.get(id=unit_id, user=user)
            material.unit = unit
        except Unit.DoesNotExist:
            return Response({"error": "Unit not found"}, status=status.HTTP_400_BAD_REQUEST)

    material.save()

    return Response(MaterialSerializer(material).data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_material_purchase(request):
    material_id = request.data.get("material")
    quantity = int(request.data.get("quantity"))
    price = int(request.data.get("price"))
    buy_at = request.data.get("buyAt")

    try:
        material = Material.objects.get(id=material_id)
    except Material.DoesNotExist:
        return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)

    purchase = MaterialPurchase.objects.create(
        material=material,
        quantity=quantity,
        price=price,
        buy_at=buy_at
    )

    serializer = MaterialPurchaseSerializer(purchase)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_material_purchase(request, purchase_id):
    try:
        purchase = MaterialPurchase.objects.get(id=purchase_id)
    except MaterialPurchase.DoesNotExist:
        return Response({"error": "Material purchase not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaterialPurchaseSerializer(purchase)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_material_purchases(request):
    user = request.user

    purchases = MaterialPurchase.objects.filter(material__user=user)
    serializer = MaterialPurchaseSerializer(purchases, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
