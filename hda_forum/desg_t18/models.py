from django.db import models
from django import forms
from django.conf import settings
# Create your models here.
class UserInformation(models.Model):
    user_name=models.CharField(max_length=15)
    first_name=models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name

class DesgT18WorkFlow(models.Model):
    track=models.CharField(max_length=200)
    title=models.CharField(max_length=500)
    gate=models.CharField(max_length=50)
    work_flow_steps=models.TextField(max_length=5000)
    image_data=models.ImageField(upload_to="desg_t18/images/",max_length=1000)
    files_data=models.FileField(upload_to="desg_t18/files/",max_length=5000)

class TriageNote(models.Model):
    sam_name=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    
    image_data=models.ImageField(upload_to="desg_t18/triage/images/",max_length=1000, blank=True)
    files_data=models.FileField(upload_to="desg_t18/triage/files/",max_length=5000, blank=True)
    updated_by=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.sam_name

class KnowledgeSharing(models.Model):
    track=models.CharField(max_length=50,blank=True)
    title=models.CharField(max_length=500,blank=True)
    question=models.CharField(max_length=500,blank=True)
    answer=models.TextField(max_length=5000,blank=True)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.question

class MeetingUpdate(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title

class OverView(models.Model):
    overview_category=models.CharField(max_length=50)
    overview_title=models.CharField(max_length=100)
    overview_content=models.TextField(max_length=5000)

    def __str__(self):
        return self.overview_category
    def get_data():
        content=OverView.objects.all()
        return content
class DesgPcUpdate(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title

class DesgGmlUpdate(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.title
