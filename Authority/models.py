from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    score = models.FloatField(default=0)


class TopCandidates(models.Model):
    number_of_selection = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)


class Authority(models.Model):

    name = models.CharField(max_length=20)
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=10)


class authority_account(models.Model):
    auth_userid = models.CharField(max_length=100, primary_key=True)
    auth_fullname = models.CharField(max_length=100, blank=False, null=False)
    auth_email = models.CharField(max_length=100, blank=False, null=False)
    auth_pass = models.CharField(max_length=10000, blank=False, null=False)
    auth_phone = models.CharField(max_length=11, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.man_pass = make_password(self.auth_pass)
        super(authority_account, self).save(*args, **kwargs)

    def __str__(self):
        return 'id: {}'.format(self.auth_userid)