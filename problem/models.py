from email.policy import default
from pyexpat import model
from random import choice, choices
from statistics import mode
from django.db import models
from pkg_resources import require

# Create your models here.


class Tag(models.Model):
    tagname = models.CharField(max_length=20)





class Problem(models.Model):

    class DifficultyLevel(models.TextChoices):
        EASY='EASY'
        MEDIUM='MEDIUM'
        HARD='HARD'
        NOTDEFINED='NOTDEFINED'

    problemcode = models.CharField(max_length=20, null=False, unique=True, default='')
    title = models.CharField(max_length=100, null=False, default='', unique=True)
    description = models.TextField(null=False)
    difficulty = models.CharField(choices=DifficultyLevel.choices, null=False, max_length=20)
    score = models.IntegerField(null=False)
    correctoutput = models.TextField(null=False, default='')


class Testcase(models.Model):
    title = models.CharField(null=False, default='', max_length=50)
    input_path = models.TextField(null=False, default='')
    output_path = models.TextField(null=False, default='')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)





class ProblemsHavingTag(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)


