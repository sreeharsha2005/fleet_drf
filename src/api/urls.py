from django.urls import path, include
from .views import VehicleView, VehicleOperatingDataView

urlpatterns = [
    path("api/v1/vehicles/", VehicleView.as_view(), name="vehicle-view"),
    path(
        "api/v1/vehicles/operatingdata/",
        VehicleOperatingDataView.as_view(),
        name="vehicle-operating-data-view",
    ),
]
