from django.db import models

# Create your models here.

class LdmForum(models.Model):
    track=models.CharField(max_length=50,blank=True)
    title=models.CharField(max_length=500,blank=True)
    question=models.CharField(max_length=500,blank=True)
    answer=models.TextField(max_length=5000,blank=True)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.question

class LdmMeetingUpdate(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=2000)
    updated_date=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.title
