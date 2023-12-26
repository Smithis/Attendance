from django.db import models
from datetime import datetime

class Rollno(models.Model):
    roll = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.now(), blank=True) 
    
    def __str__(self):
        return self.roll
