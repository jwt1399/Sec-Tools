from datetime import datetime

from django.db import models
import time

# Create your models here.
class Middleware_vuln(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, null=True)
    result = models.CharField(max_length=100, null=True)
    CVE_id = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True, unique=True)
