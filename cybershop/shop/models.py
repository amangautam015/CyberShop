from django.conf import settings
from django.db import models
from django.dispatch import receiver
import os
from django.utils import timezone
from .validator import validate_file_extension
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class shop_user(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField()
    password = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    ship_address = models.TextField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Image(models.Model):
    document =  models.FileField(_("file"), upload_to='images/', validators=[validate_file_extension])

class product(models.Model):
    SIZE = ['SM','M','L','XL']
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    is_size_specific = models.BooleanField(default=False)
    size = models.CharField(blank=True,choices=SIZE,null=True,default=None)
    description = models.TextField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.name

class order(models.Model):
    STATUS = ['PROCESSING','DELIVERED','CANCELLED']
    created_date = models.DateField()
    product = models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shop = models.ForeignKey(shop_user,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS,blank=True,null=True,default=None)
    def create(self):
        self.created_date = timezone.now()
        self.save()



