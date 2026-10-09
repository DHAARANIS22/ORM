from django.db import models
from django.contrib import admin
class customer(models.Model):
    Customer_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    productname=models.IntegerField()
    phoneno=models.IntegerField()
    Email=models.TextField()
    address=models.TextField()
    pincode=models.IntegerField()
class customerAdmin(admin.ModelAdmin):
    list_display=["Customer_id","Name","productname","phoneno","Email","address","pincode"]

