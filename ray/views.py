from django.shortcuts import render
from ray.models import *
import datetime

def getScheduleBetween(s_date, e_date, doc_id):
    return Appointment.objects.filter(scheduled_at__gt = s_date, scheduled_till__lt = e_date, doctor=Doctor.objects.get(id=doc_id), cancelled=False)

def getScheduleDay(s_date, doc_id):
    return Appointment.objects.filter(scheduled_at__year = s_date.year, scheduled_at__month = s_date.month, scheduled_at__day = s_date.day, doctor=Doctor.objects.get(id=doc_id), cancelled=False)

def cancelAppointments(s_date, reason, doc_id):
    return getScheduleDay(s_date, doc_id).update(cancelled=True, cancelled_reason=reason, doctor=Doctor.objects.get(id=doc_id))

def postponeAppointments(s_date, doc_id, time, type):
    for x in getScheduleDay(s_date, doc_id):
        if type == 'min':
            x.scheduled_at = x.scheduled_at + datetime.timedelta(minutes = time)
            x.save()
        if type == 'hr':
            x.scheduled_at = x.scheduled_at + datetime.timedelta(hours = time)
            x.save()

def preponeAppointments(s_date, doc_id, time, type):
    for x in getScheduleDay(s_date, doc_id):
        if type == 'min':
            x.scheduled_at = x.scheduled_at - datetime.timedelta(minutes = time)
            x.save()
        if type == 'hr':
            x.scheduled_at = x.scheduled_at - datetime.timedelta(hours = time)
            x.save()
