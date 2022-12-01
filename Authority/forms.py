from django import forms
from django.db import models
from django.db.models import fields
from . models import authority_account


class authority_account_form(forms.ModelForm):
    auth_email = forms.CharField(widget=forms.EmailInput())
    auth_pass = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = authority_account
        fields = [
            'auth_userid',
            'auth_fullname',
            'auth_email',
            'auth_phone',
            'auth_pass'
        ]


class authority_login_raw_form(forms.Form):
    auth_userid = forms.CharField()
    auth_pass = forms.CharField(widget=forms.PasswordInput())

