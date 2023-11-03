from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class YogaLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reminder = models.CharField(max_length=200, null=True, blank=True)
    time = models.IntegerField(null=True, blank=True, default=0)
    # completedAt = models.DateTimeField(auto_now_add=True)
    completedAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.user)
    