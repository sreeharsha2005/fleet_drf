from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
