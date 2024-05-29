from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'category_slug':('category_name',)}
    list_display = ['category_name']


admin.site.register(Category,CategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductVariationInline]
    list_display = ('product_name', 'price', 'stock', 'is_available', 'category', 'brand', 'created_date', 'modified_date')
    prepopulated_fields = {'product_slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)




class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'brand_slug':('brand_name',)}
    list_display = ['brand_name','brand_category']


admin.site.register(Brand,BrandAdmin)