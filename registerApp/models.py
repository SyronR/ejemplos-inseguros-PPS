from django.db import models
from django import forms


class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=50, unique=True)
    password = models.TextField(max_length=50)


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
