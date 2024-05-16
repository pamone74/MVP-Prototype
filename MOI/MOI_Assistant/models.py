from django.db import models

class Consumers(models.Model):
    name = models.CharField(max_length=100)
    EID = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    driver_license = models.CharField(max_length=100)
    traffic_fine = models.CharField(max_length=100, default='No fines')
    drivers_expiry_date = models.DateField()
    vehicle_registration = models.CharField(max_length=100)
    criminal_record_certificate = models.CharField(max_length=100, default='No criminal record')
    vehicle_registration_expiry_date = models.DateField(default='2021-12-12')
