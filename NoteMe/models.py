from django.db import models
from django.contrib.auth.models import User


class MyNotes(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=255)
    note = models.CharField(max_length=2000)
