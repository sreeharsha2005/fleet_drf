from src.api.serializers.vehicle_operating_data_serializer import (
    VehicleOperatingDataSerializer,
)

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema


class VehicleOperatingDataListView(APIView):
    serializer_class = VehicleOperatingDataSerializer

    @extend_schema(
        tags=["Vehicle"],
        summary="Get Vehicle Operating Data List",
    )
    def get(self, request):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Vehicle"],
        summary="Create new Vehicle Operating Data record",
    )
    def post(self, request):
        serializer = VehicleOperatingDataSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                dict(errors=serializer.errors), status=status.HTTP_400_BAD_REQUEST
            )

        resp = serializer.create(serializer.validated_data)

        if resp is None:
            return Response("Error writing to db", status=status.HTTP_400_BAD_REQUEST)
        else:
            resp_obj = dict(
                vin=resp.vin,
                timestamp=resp.timestamp,
                tire_pressure=resp.tire_pressure.attribute_values,
                collision_alerts=resp.collision_alerts.attribute_values,
            )

            return Response(resp_obj, status=status.HTTP_201_CREATED)


class VehicleOperatingDataDetailView(APIView):
    serializer_class = VehicleOperatingDataSerializer

    @extend_schema(
        tags=["Vehicle"],
        summary="Retrieve Vehicle Operating Data with given Id",
    )
    def get(self, request, vehicle_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Vehicle"],
        summary="Update Vehicle Operating Data with given Id",
    )
    def patch(self, request, vehicle_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Vehicle"],
        summary="Delete Vehicle Operating Data with given Id",
    )
    def delete(self, request, vehicle_id):
        return Response("", status=status.HTTP_200_OK)
