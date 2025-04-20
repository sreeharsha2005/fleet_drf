from rest_framework import serializers
from src.api.models.vehicle_model import Vehicle
from src.pynamo_db.models.vehicleDB import VehicleDB

import base64

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        exclude = ["id"]

    def validate_year(self, value):
        if value < 0 or value > 9999:
            return serializers.ValidationError("Year should be between [1800 - 2100]")
        return value

    def create(self, validated_data):
        vehicle_data = validated_data

        # Decoded VIN
        decoded_vin = base64.b64decode(vehicle_data["vin"])
        vehicle_data["vin"] = str(decoded_vin.decode("utf-8"))

        vehicle_obj = VehicleDB(
            vin=vehicle_data["vin"],
            year=vehicle_data["year"],
            make=vehicle_data["make"],
            model=vehicle_data["model"],
        )

        vehicle_obj.save()

        for item in VehicleDB.scan():
            if item.vin == vehicle_data["vin"]:
                return item

        return None
