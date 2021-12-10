from django.db import models

# Create your models here.

class Job(models.Model):
    summary = models.CharField(max_length=1000)
    github_url = models.URLField(max_length=100, null=True)
    
