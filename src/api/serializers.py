from rest_framework import serializers
from .models import Vehicle, VehicleOperatingData, TpmsData, CollisionAlerts
from src.pynamo_db.models.vehicleDB import VehicleDB
from src.pynamo_db.models.vehicleOperatingDataDB import VehicleOperatingDataDB

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


class TpmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TpmsData
        fields = '__all__'

class CollisionAlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollisionAlerts
        fields = '__all__'

class VehicleOperatingDataSerializer(serializers.ModelSerializer):
    tire_pressure = TpmsSerializer()
    collision_alerts = CollisionAlertsSerializer()

    class Meta:
        model = VehicleOperatingData
        exclude = ["id"]

    def create(self, validated_data):
        vehicle_operating_data = validated_data

        # Decoded VIN
        decoded_vin = base64.b64decode(vehicle_operating_data["vin"])
        vehicle_operating_data["vin"] = str(decoded_vin.decode("utf-8"))

        vehicle_oper_data_obj = VehicleOperatingDataDB(
            vin=vehicle_operating_data["vin"],
            timestamp=vehicle_operating_data["timestamp"],
            tire_pressure=vehicle_operating_data["tire_pressure"],
            collision_alerts=vehicle_operating_data["collision_alerts"],
        )

        vehicle_oper_data_obj.save()

        for item in VehicleOperatingDataDB.scan():
            if item.vin == vehicle_operating_data["vin"]:
                return item

        return None
