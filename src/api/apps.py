import sys

from django.apps import AppConfig
from src.pynamo_db.models.vehicleDB import VehicleDB
from src.pynamo_db.models.vehicleOperatingDataDB import VehicleOperatingDataDB

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.api'


    def create_db_tables(self):
        """
        Create a required dynamodb tables
        """
        try:
            # Create Vehicle table
            if not VehicleDB.exists():
                VehicleDB.create_table(wait=True)
                print("Vehicle Table Created..........................")
            else:
                print("Vehicle Table already exists")
        except:
            print("Vehicle Table creation error. Check if dynamodb-local is running")

        try:
            if not VehicleOperatingDataDB.exists():
                VehicleOperatingDataDB.create_table(wait=True)
                print("Vehicle Operating Data Table Created............")
            else:
                print("Vehicle Operating Data Table already exists")
        except:
            print(
                "Vehicle Operating Data Table creation error. Check if dynamodb-local is running"
            )

        return

    def ready(self):
        """
        Server starts
        """
        if "runserver" not in sys.argv:
            return True

        self.create_db_tables()
