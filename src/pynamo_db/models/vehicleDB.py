from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class VehicleDB(Model):
    """
    Vehicle table
    """

    class Meta:
        aws_access_key_id = "08qlka"
        aws_secret_access_key = "suyfvm"
        read_capacity_units = 1
        write_capacity_units = 1
        table_name = "vehicle"
        region = "localhost"
        host = "http://localhost:8000"

    vin = UnicodeAttribute(hash_key=True)
    year = NumberAttribute(range_key=True)
    make = UnicodeAttribute()
    model = UnicodeAttribute()

