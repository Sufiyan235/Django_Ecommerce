from django.db import models
from store_app.models import *
from account.models import Account
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItems, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=20,null=True,blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, default='pending')
    address=models.TextField(max_length=500)
    country=models.CharField(max_length=20,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    zip_code=models.CharField(max_length=20,null=True,blank=True)
    is_paid = models.BooleanField(default=False,null=True,blank=True)