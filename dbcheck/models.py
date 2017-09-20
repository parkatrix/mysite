from django.db import models
from django.utils import timezone
# Create your models here.

class Instance(models.Model) :
    instancename = models.CharField(max_length=100)
    servername = models.CharField(max_length=100)
    ipaddr=models.CharField(max_length=30)
    port=models.CharField(max_length=10)
    ms=models.CharField(max_length=1000,null=True)
    updated_date=models.DateTimeField(blank=True,default=timezone.now)

    def __str__(self):
        return self.instancename
