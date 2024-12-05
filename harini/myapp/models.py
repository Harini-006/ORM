from django.db import models
from django.contrib import admin
# Create your models here.
class Bankloan(models.Model):
    LOAN_ID=models.IntegerField(primary_key=True)
    CUST_NAME=models.CharField(max_length=100)
    LOAN_TYPE=models.CharField(max_length=100)
    CUST_ACNO=models.IntegerField()
    LOAN_AMT=models.IntegerField()
class loan(admin.ModelAdmin):
    list_display=("LOAN_ID","CUST_NAME","LOAN_TYPE","CUST_ACNO","LOAN_AMT")