from src.api.serializers.vehicle_serializer import VehicleSerializer

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema


class VehicleListView(APIView):
    serializer_class = VehicleSerializer

    @extend_schema(
        tags=["Vehicle"],
        summary="Get Vehicle List",
    )
    def get(self, request):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Vehicle"],
        summary="Create new Vehicle record",
        description="This endpoint allows you to create a new vehicle. You must provide vehicle details",
        request=VehicleSerializer,
        responses={201: VehicleSerializer, 404: ""},
    )
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                dict(errors=serializer.errors), status=status.HTTP_400_BAD_REQUEST
            )

        resp = serializer.create(serializer.validated_data)
        if resp is None:
            return Response("Error writing to db", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(resp.attribute_values, status=status.HTTP_201_CREATED)


class VehicleDetailView(APIView):
    serializer_class = VehicleSerializer

    @extend_schema(
        tags=["Vehicle"],
        summary="Retrieve Vehicle with given Id",
    )
    def get(self, request, vehicle_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Vehicle"],
        summary="Update Vehicle with given Id",
    )
    def patch(self, request, vehicle_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Vehicle"],
        summary="Delete Vehicle with given Id",
    )
    def delete(self, request, vehicle_id):
        return Response("", status=status.HTTP_200_OK)
