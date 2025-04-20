from src.api.serializers.vehicle_serializer import VehicleSerializer

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema


class DriverProfileDataListView(APIView):
    serializer_class = VehicleSerializer

    @extend_schema(
        tags=["DriverProfile"],
        summary="Create new Driver Profile Data record",
    )
    def post(self, request):
        return Response("", status=status.HTTP_201_CREATED)

    @extend_schema(
        tags=["DriverProfile"],
        summary="Get Driver Profile Data List",
    )
    def get(self, request):
        return Response("", status=status.HTTP_200_OK)


class DriverProfileDataDetailView(APIView):
    serializer_class = VehicleSerializer

    @extend_schema(
        tags=["DriverProfile"],
        summary="Retrieve Driver Profile Data with given Id",
    )
    def get(self, request, driver_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["DriverProfile"],
        summary="Update Driver Profile Data with given Id",
    )
    def patch(self, request, driver_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["DriverProfile"],
        summary="Delete Driver Profile Data with given Id",
    )
    def delete(self, request, driver_id):
        return Response("", status=status.HTTP_200_OK)
