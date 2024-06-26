from django.contrib import admin
from .models import*
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display =['user','order_date','order_number','total_price','status','is_paid']


admin.site.register(Order,OrderAdmin)