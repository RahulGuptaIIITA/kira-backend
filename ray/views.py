from django.shortcuts import render
from ray.models import *

def getScheduleBetween(s_date, e_date, doc_id):
    appointments_between = Appointment.objects.filter(scheduled_at__gt = s_date, scheduled_till__lt = e_date, doctor=Doctor.objects.get(id=doc_id));

    return appointments_between

def getScheduleDay(s_date, doc_id):
    return Appointment.objects.filter(scheduled_at__year = s_date.year, scheduled_at__month = s_date.month, scheduled_at__day = s_date.day, doctor=Doctor.objects.get(id=doc_id))

def cancelAppointments(s_date, reason, doc_id):
    app = getScheduleDay(s_date).update(cancelled=True, cancelled_reason=reason, doctor=Doctor.objects.get(id=doc_id))

    return app
