
from django.contrib.auth.models import User
from django.db import models


class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)