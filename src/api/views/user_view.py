from src.api.serializers.vehicle_serializer import VehicleSerializer

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema


class UserDataListView(APIView):
    serializer_class = VehicleSerializer

    @extend_schema(
        tags=["User"],
        summary="Create new User Data record",
    )
    def post(self, request):
        return Response("", status=status.HTTP_201_CREATED)

    @extend_schema(
        tags=["User"],
        summary="Get User Data List",
    )
    def get(self, request):
        return Response("", status=status.HTTP_200_OK)


class UserDataDetailView(APIView):
    serializer_class = VehicleSerializer

    @extend_schema(
        tags=["User"],
        summary="Retrieve User Data with given Id",
    )
    def get(self, request, user_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["User"],
        summary="Update User Data with given Id",
    )
    def patch(self, request, user_id):
        return Response("", status=status.HTTP_200_OK)

    @extend_schema(
        tags=["User"],
        summary="Delete User Data with given Id",
    )
    def delete(self, request):
        return Response("", status=status.HTTP_200_OK)


