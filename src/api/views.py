from .serializers import VehicleSerializer, VehicleOperatingDataSerializer

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

class VehicleView(APIView):
    serializer_class = VehicleSerializer

    @extend_schema(
        tags=["Vehicles"],
        summary="Create a new Vehicle",
        description="This endpoint allows you to create a new vehicle. You must provide vehicle details",
        request=VehicleSerializer,
        responses={201: VehicleSerializer,
                   404: ""},
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


class VehicleOperatingDataView(APIView):
    serializer_class = VehicleOperatingDataSerializer

    @extend_schema(
        tags=["Vehicles"]
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
