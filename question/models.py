from django.db import models

TASK_CHOICES = (
    ('T', 'Today'),
    ('M', 'Tomorrow'),
    ('C', 'Clear'),
    ('P', 'Prescription'),
    ('B', 'Billing'),
    ('D', 'GetDrugInfo'),
    ('S', 'SuggestDrug'),
    ('O', 'Clashes')
)

class Question(models.Model):
    question_text = models.CharField(max_length=2000)
    task = models.CharField(max_length=1, choices=TASK_CHOICES)

    def __str__(self):
        return self.question_text
