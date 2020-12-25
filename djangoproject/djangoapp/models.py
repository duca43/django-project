from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    NORMAL_PRIORITY = 'NP'
    CRITICAL_PRIORITY = 'CP'

    PRIORITY_CHOICES = [
        (NORMAL_PRIORITY, 'Normal'),
        (CRITICAL_PRIORITY, 'Critical'),
    ]

    title = models.CharField(max_length=50)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default=NORMAL_PRIORITY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

