from django.db import models
from django.forms import ModelForm


class UploadFile(models.Model):
    title = models.CharField(max_length=50)
    file = models.CharField(max_length=100)




class ReviewMessage(models.Model):
    fullName = models.CharField(max_length=200)
    emailAddress = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    emailSubject = models.CharField(max_length=200)
    emailMessage = models.CharField(max_length=1000)