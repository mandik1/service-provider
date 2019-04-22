from django.db import models
from django import forms
from django.forms import ModelForm,MultipleChoiceField
from django.shortcuts import render, reverse
from django.contrib.auth.models import User

    # def get_absolute_url(self):
    #     return reverse('serviceslist')

class Userdata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phn = models.IntegerField()
    address = models.CharField(max_length = 200)

class Services(models.Model):
    servicename = models.CharField(max_length = 50)
    image = models.FileField()
    price = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.servicename


class Appointement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    when = models.DateField()
    address = models.CharField(max_length=25, null=True, blank=True)
    objects = models.Manager()  


class PaymentMode(models.Model):
    modename = models.CharField(max_length=50)

    def __str__(self):
        return self.modename


# class Payment(models.Model):
#     cardholder = models.CharField(30)
#     cardnumber = models.IntegerField(30)
#     validitiy = models.DateField()
    