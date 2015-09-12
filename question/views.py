from django.shortcuts import render
from .models import Question
from fuzzywuzzy import process
from ray.views import cancelAppointments, getScheduleDay

# Create your views here.

def command(request):
    c_text = request.POST['command']
    command_bank = [q.question_text for q in Question.objects.all().values('question_text')]
    task = Question.objects.get(question_text=process.extract(command, command_bank)[0][0]).task

    if task === 'T':
        return getScheduleDay(datetime.date.today())
