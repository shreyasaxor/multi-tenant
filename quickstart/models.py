# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class State(models.Model):
    """ This Table contains states-provinces seed-data for the respective countries """
    name = models.CharField(max_length=250)
    state_code = models.CharField(max_length=10)


class Education(models.Model):
    """Education Details"""
    name = models.CharField(max_length=250)


class Skill(models.Model):
    """SKills data"""
    name = models.CharField(max_length=50, unique=True)

class Time(models.Model):
    time = models.IntegerField()

