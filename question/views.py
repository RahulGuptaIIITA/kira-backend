from django.shortcuts import render
from .models import Question
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from ray.views import cancelAppointments, getScheduleDay, postponeAppointments
from django.core import serializers
from django.http import HttpResponse
import datetime
from nltk.corpus import stopwords
from ray.models import *
import nltk

def command(request):
    c_text = request.GET['command']
    word_list_post_pre = nltk.word_tokenize(c_text)
    if 'postpone' in word_list_post_pre:
        postpone_data = post_pone_time(c_text)
        return HttpResponse('{\"message\":\"'+postpone_data+'\"}', mimetype="application/json")

    if 'prepone' in word_list_post_pre:
        if 'tomorrow' in word_list_post_pre:
            postpone_data = prepone_time(c_text)
            return HttpResponse('{\"message\":\"'+postpone_data+'\"}', mimetype="application/json")

    if c_text == 'reset everything':
        Appointment.objects.update(cancelled=False)
        return HttpResponse('{\"message\":\"Made everything non-cancelled\"}', mimetype="application/json")
    command_bank = [q.question_text for q in Question.objects.all()]
    if process.extract(c_text, command_bank)[0][1] < 50:
        return HttpResponse('{\"message\":\"Not A Good String\"}', mimetype="application/json")
    task = Question.objects.get(question_text=process.extract(c_text, command_bank)[0][0]).task

    if task == 'T':
        return HttpResponse('{\"data\":'+serializers.serialize('json', getScheduleDay(datetime.date.today(), 1))+'}', mimetype="application/json")

    elif task == 'M':
        return HttpResponse('{\"data\":'+serializers.serialize('json', getScheduleDay((datetime.date.today() + datetime.timedelta(days=1)), 1))+'}', mimetype="application/json")

    elif task == 'CT':
        cancelled = cancelAppointments(datetime.date.today(),'I\'m sick', 1)
        return HttpResponse('{\"message\":\"Cancelled today\'s appointments\"}', mimetype="application/json")

    elif task == 'CM':
        cancelled = cancelAppointments((datetime.date.today() + datetime.timedelta(days=1)), 'I\'m sick', 1)
        return HttpResponse('{\"message\":\"Cancelled tomorrow\'s appointments\"}', mimetype="application/json")

def prescription(raw_text):
    word_list = nltk.word_tokenize(raw_text)
    filtered_word_list = word_list[:]
    for word in word_list:
        if word in stopwords.words('english'):
            filtered_word_list.remove(word)
    time_stack = []
    pill_stack = []
    master_timings = ["morning", "afternoon", "evening", "night", "before sleeping", "before lunch", "after lunch", "before dinner", "after dinner"]
    for i in range(len(filtered_word_list)):
        if (fuzz.partial_ratio(filtered_word_list[i], "mg") >= 95) or (fuzz.partial_ratio(filtered_word_list[i], "milligrams") >= 95):
            if i!=0 and filtered_word_list[i-1].isdigit():
                dosage = filtered_word_list[i-1]
                filtered_word_list.remove(dosage)
    for word in filtered_word_list:
        if word.isDigit():
            pill_stack.append(word)
        if word in master_timings:
            time_stack.append()

def post_pone_time(raw_text):
    time_words = ['minutes', 'hours']
    word_list = nltk.word_tokenize(raw_text)
    time_it = ''
    number_it = 0
    for word in word_list:
        if (fuzz.partial_ratio(word, "minutes") >= 95):
            time_it = 'min'
        elif (fuzz.partial_ratio(word, "hours") >= 95):
            time_it = 'hr'
        try:
            number_it = int(word)
        except ValueError:
            pass
    today = datetime.date.today()
    if time_it != '' and number_it != 0:
        postponeAppointments(today, 1, number_it, time_it)
        if time_it == 'hr':
            return "postponed by "+str(number_it)+' hours'
        else:
            return "postponed by "+str(number_it)+' minutes'

    return "Nothing Postponed. Try again"

def prepone_time(raw_text):
    time_words = ['minutes', 'hours']
    word_list = nltk.word_tokenize(raw_text)
    time_it = ''
    number_it = 0
    for word in word_list:
        if (fuzz.partial_ratio(word, "minutes") >= 95):
            time_it = 'min'
        elif (fuzz.partial_ratio(word, "hours") >= 95):
            time_it = 'hr'
        try:
            number_it = int(word)
        except ValueError:
            pass
    today = datetime.date.today()+datetime.timedelta(days = 1)
    if time_it != '' or time_it:
        postponeAppointments(today, 1, number_it, time_it)
        if time_it == 'hr':
            return "preponed by "+str(number_it)+' hours'
        else:
            return "preponed by "+str(number_it)+' minutes'
