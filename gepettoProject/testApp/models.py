from django.db import models
from mainApp.models import *
from django.conf import settings

class Test(models.Model):
    ANSWER = [
        ('O', 'O'),
        ('X', 'X'),
    ]
    tester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    answer1 = models.CharField(
        max_length = 1,
        choices = ANSWER,
        default = 'O',
    )
    answer2 = models.CharField(
        max_length = 1,
        choices = ANSWER,
        default = 'O',
    )
    answer3 = models.CharField(
        max_length = 1,
        choices = ANSWER,
        default = 'O',
    )
    test_probability = models.CharField(
        max_length = 80,
        default = 0,
    )
