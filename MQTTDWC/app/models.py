"""
Definition of models.
"""

from django.db import models
# Create your models here.

class Message(models.Model):
    topic = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
    message_string = models.CharField(max_length=100)
