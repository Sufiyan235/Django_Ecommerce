from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'category_slug':('category_name',)}
    list_display = ['category_name']


admin.site.register(Category,CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'brand_slug':('brand_name',)}
    list_display = ['brand_name','brand_category']


admin.site.register(Brand,BrandAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class AvailableDesignInline(admin.TabularInline):
    model = AvailableDesign
    extra = 1

# Admin class for Product with inlines for ProductImage and ProductVariation
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,AvailableDesignInline]
    list_display = ('product_name', 'price', 'stock', 'is_available', 'category', 'brand' )
    prepopulated_fields = {'product_slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)


class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name','price']

admin.site.register(ColorVariant,ColorVariantAdmin)

class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name','price']

admin.site.register(SizeVariant,SizeVariantAdmin)



class CartAdmin(admin.ModelAdmin):
    list_display = ["user",'is_paid']

admin.site.register(Cart,CartAdmin)

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart','product','color_variant','size_variant']

admin.site.register(CartItems,CartItemsAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display =['coupon_name','discount_amount','minimum_amount','is_expired']


admin.site.register(Coupon,CouponAdmin)

