from django.db import models

# Create your models here.

class Company(models.Model):
    id=models.AutoField(primary_key=True)
    client_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
    created_by=models.CharField(max_length=50)
