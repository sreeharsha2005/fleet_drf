from rest_framework import serializers
from src.api.models.vehicle_operating_data_model import VehicleOperatingData, TpmsData, CollisionAlerts
from src.pynamo_db.models.vehicleOperatingDataDB import VehicleOperatingDataDB

import base64

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
