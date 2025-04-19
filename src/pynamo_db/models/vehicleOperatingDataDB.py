from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
    MapAttribute,
    UTCDateTimeAttribute,
)


class TpmsData(MapAttribute):

    tpms_fl = NumberAttribute(default=0)
    tpms_fr = NumberAttribute(default=0)
    tpms_rl = NumberAttribute(default=0)
    tpms_rr = NumberAttribute(default=0)


class CollisionAlerts(MapAttribute):

    front = NumberAttribute(default=0)
    right = NumberAttribute(default=0)
    left = NumberAttribute(default=0)
    back = NumberAttribute(default=0)


class VehicleOperatingDataDB(Model):
    """
    Vehicle table
    """

    class Meta:
        aws_access_key_id = "08qlka"
        aws_secret_access_key = "suyfvm"
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "vehicle_operating_data"
        region = "localhost"
        host = "http://localhost:8000"

    vin = UnicodeAttribute(hash_key=True)
    timestamp = NumberAttribute(range_key=True)
    tire_pressure = TpmsData()
    collision_alerts = CollisionAlerts()
