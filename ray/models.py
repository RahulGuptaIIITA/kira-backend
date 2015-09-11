from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=70)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    treatmentPlanName = models.CharField(max_length=200)
    cancelled = models.BooleanField(default=False)
    cancelled_reason = models.CharField(max_length=200)
    start = models.DateTimeField(auto_now_add=True)
    photo_url = models.CharField(max_length=200)
    has_photo = models.BooleanField()

    def __str__(self):
        return self.patient

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment)
    drug = models.CharField(max_length=200)
    dosage = models.CharField(max_length=1000)

    def __str__(self):
        return self.appointment
