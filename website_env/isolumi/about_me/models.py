""" models.py """
from django.db import models


class AboutMe(models.Model):
    """ About Me"""
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
