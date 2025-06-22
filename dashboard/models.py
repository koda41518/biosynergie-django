from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    ph = models.FloatField()
    pressure = models.FloatField()
    sun_intensity = models.FloatField(null=True, blank=True)
    methane_production = models.FloatField(null=True, blank=True)
    solar_production = models.FloatField(null=True, blank=True)
    algae_activity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp} | Temp: {self.temperature}°C | pH: {self.ph}"