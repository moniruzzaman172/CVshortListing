from datetime import datetime
from django.db import models


class Resume(models.Model):
    resumeId = models.AutoField(primary_key=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)


class Candidate(models.Model):
    candidateId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    total_experiences = models.FloatField()
    total_skills = models.IntegerField()
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    skills_score = models.FloatField()
    experiences_skills_combined_score = models.FloatField()


class Personal(models.Model):

    email = models.EmailField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.email
