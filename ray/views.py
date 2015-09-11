from django.shortcuts import render
from ray.models import *

def getScheduleBetween(s_date, e_date):
    appointments_between = Appointment.objects.filter(scheduled_at__gt = s_date, scheduled_till__lt = e_date);

    return appointments_between

def getScheduleDay(s_date):
    return Appointment.objects.filter(scheduled_at__year = s_date.year, scheduled_at__month = s_date.month, scheduled_at__day = s_date.day)

def cancelAppointments(s_date, reason):
    app = getScheduleDay(s_date).update(cancelled=True, cancelled_reason=reason)

    return app
