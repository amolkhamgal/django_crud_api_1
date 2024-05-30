from django.db import models

# Create your models here.

class Employee(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    dept=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.IntegerField(default=0)
