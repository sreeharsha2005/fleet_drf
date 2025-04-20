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


