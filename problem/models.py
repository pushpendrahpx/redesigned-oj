from email.policy import default
from pyexpat import model
from random import choice, choices
from statistics import mode
from django.db import models

# Create your models here.


class Tags(models.Model):
    tagname = models.CharField(max_length=20)


class Problem(models.Model):

    class DifficultyLevel(models.TextChoices):
        EASY='EASY'
        MEDIUM='MEDIUM'
        HARD='HARD'
        NOTDEFINED='NOTDEFINED'

    description = models.TextField(null=False)
    difficulty = models.CharField(choices=DifficultyLevel.choices, null=False, max_length=20)
    score = models.IntegerField(null=False)
    

class ProblemsHavingTags(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)


