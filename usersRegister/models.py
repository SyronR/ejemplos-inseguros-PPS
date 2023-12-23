from django.db import models


class Usuario(models.Model):

    username = models.TextField(unique=True, max_length=50, primary_key=True)
    password = models.TextField(max_length=50)
