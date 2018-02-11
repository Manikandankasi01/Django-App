from django.db import models
from django import forms
# Create your models here.


'''
DESG Automation Model
'''
class DesgAutomationUpdate(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.title

class DesgAutomationRelease(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title

'''
PDC Automation Model
'''

class PdcAutomationUpdate(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.title

class PdcAutomationRelease(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title


'''
LDM Automation Model
'''

class LdmAutomationUpdate(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.title

class LdmAutomationRelease(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title