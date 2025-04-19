from django.db import models

# Create your models here.
# Create your models here.

"""
To start dynamodb-local on mac
docker run -d -p 8000:8000 amazon/dynamodb-local

To view the dynamodb tables on web-browser
npm install -g dynamodb-admin
AWS_REGION=localhost AWS_ACCESS_KEY_ID=08qlka AWS_SECRET_ACCESS_KEY=suyfvm dynamodb-admin

~ AWS_REGION=localhost AWS_ACCESS_KEY_ID=08qlka AWS_SECRET_ACCESS_KEY=suyfvm dynamodb-admin

  database endpoint: 	http://localhost:8000
  region: 		localhost
  accessKey: 		08qlka

  dynamodb-admin listening on http://:::8001 (alternatively http://0.0.0.0:8001)
"""

"""
To view the dynamob tables on NoSQL Workbench
Create a connection and use the same access_key and secret_key to create the tables
region=localhost for NoSQL Workbench
"""

# from .db_models.vehicle_model import Vehicle

# if not Vehicle.exists():
#     Vehicle.create_table(wait=True)
# else:
#     print("Table already exists")

# veh_item1 = Vehicle(
#     vin = "efgh",
#     year = 2025,
#     make="RIVIAN",
#     model="R1S"
# )

# veh_item2 = Vehicle(
#     vin = "ABCD",
#     year = 2025,
#     make="RIVIAN",
#     model="R1T"
# )

# veh_item1.save()
# veh_item2.save()

# for item in Vehicle.scan():
#     print(item)

# print("Table size: {}".format(Vehicle.describe_table().get('ItemCount')))

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Vehicle(models.Model):
    """
    Vehicle REST API model
    """

    vin = models.CharField(max_length=32)
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)

    def get(self):
        vehicle_data_dict = dict(
            vin=self.vin, year=self.year, make=self.make, model=self.model
        )
        return vehicle_data_dict


class TpmsData(models.Model):
    """
    Vehicle TPMS Data REST API model
    """

    tpms_fl = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(350), MaxValueValidator(450)]
    )
    tpms_fr = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(350), MaxValueValidator(450)]
    )
    tpms_rl = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(350), MaxValueValidator(450)]
    )
    tpms_rr = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(350), MaxValueValidator(450)]
    )

    def get(self):
        tpms_data_dict = dict(
            tpms_fl=self.tpms_fl,
            tpms_fr=self.tpms_fr,
            tpms_rl=self.tpms_rl,
            tpms_rr=self.tpms_rr,
        )
        return tpms_data_dict


class CollisionAlerts(models.Model):
    """
    Vehicle Collision Alerts REST API model
    """

    front = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(25)]
    )
    right = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(25)]
    )
    left = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(25)]
    )
    back = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(25)]
    )

    def get(self):
        collision_alerts_dict = dict(
            front=self.front, right=self.right, left=self.left, back=self.back
        )
        return collision_alerts_dict


class VehicleOperatingData(models.Model):
    """
    Vehicle Operating Data RESPT API model
    """

    vin = models.CharField(max_length=32)
    timestamp = models.PositiveIntegerField()
    tire_pressure = TpmsData()
    collision_alerts = CollisionAlerts()

    def get(self):
        vehicle_oper_data_dict = dict(
            vin=self.vin,
            timestamp=self.timestamp,
            tire_pressure=self.tire_pressure.__dict__,
            collision_alerts=self.collision_alerts.__dict__,
        )
        print("getting the data from here", vehicle_oper_data_dict)

        return vehicle_oper_data_dict
