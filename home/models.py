from django.db import models
from django import forms
import pyowm
from pyowm.utils import timestamps
import time
from datetime import timedelta, datetime
# import matplotlib.pyplot as plt
from PIL import ImageTk,Image
from collections import namedtuple


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
class Search(models.Model):
    Location=models.CharField(max_length=200)

    def __str__(self):
        return self.Location