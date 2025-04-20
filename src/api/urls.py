from django.urls import path, include
from src.api.views.driver_profile_view import (
    DriverProfileDataListView,
    DriverProfileDataDetailView,
)
from src.api.views.user_view import UserDataListView, UserDataDetailView
from src.api.views.vehicle_view import VehicleListView, VehicleDetailView
from src.api.views.vehicle_operating_data_view import (
    VehicleOperatingDataListView,
    VehicleOperatingDataDetailView,
)

urlpatterns = [
    path("api/v1/vehicle/", VehicleListView.as_view(), name="vehicle-list-view"),
    path(
        "api/v1/vehicle/<int:vehicle_id>",
        VehicleDetailView.as_view(),
        name="vehicle-list-view",
    ),
    path(
        "api/v1/vehicle/operatingdata/",
        VehicleOperatingDataListView.as_view(),
        name="vehicle-operating-data-list-view",
    ),
    path(
        "api/v1/vehicle/operatingdata/<int:vehicle_id>",
        VehicleOperatingDataDetailView.as_view(),
        name="vehicle-operating-data-detail-view",
    ),
    path("api/v1/user/", UserDataListView.as_view(), name="user-data-list-view"),
    path(
        "api/v1/user/<int:user_id>",
        UserDataDetailView.as_view(),
        name="user-data-list-view",
    ),
    path(
        "api/v1/driverprofile/",
        DriverProfileDataListView.as_view(),
        name="driver-profile-list-view",
    ),
    path(
        "api/v1/driverprofile/<int:driver_id>",
        DriverProfileDataDetailView.as_view(),
        name="driver-profile-detail-view",
    ),
]
