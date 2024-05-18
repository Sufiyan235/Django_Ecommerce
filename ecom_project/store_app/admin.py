from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'category_slug':('category_name',)}
    list_display = ['category_name']


admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','category']

admin.site.register(Product,ProductAdmin)