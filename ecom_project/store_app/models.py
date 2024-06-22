from django.db import models
from account.models import Account
# Create your models here.


class Category(models.Model):
    category_slug = models.SlugField(max_length=50)
    category_name = models.CharField(max_length=100)
    category_desc =models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='categories_image',null=True,blank=True)

    def __str__(self):
        return self.category_name
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_image = models.ImageField(upload_to="Brand logos")
    brand_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand_slug = models.SlugField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.brand_name
    

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.color_name
    

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    product_image = models.ImageField(upload_to="Product_Images")
    product_slug = models.SlugField(max_length=50,unique=True)
    color_variant = models.ManyToManyField(ColorVariant,blank=True)
    size_variant = models.ManyToManyField(SizeVariant,blank=True)
    # description=models.TextField(max_length=300,blank=True)
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    

    def get_product_price_by_size(self,size):
        return self.price + SizeVariant.objects.get(size_name=size).price

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product_Images')

    def __str__(self):
        return f"{self.product.product_name}"
    
class AvailableDesign(models.Model):
    available_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product_Images',null=True,blank=True)



class Cart(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    

    # def get_cart_total(self):
    #     cart_items = CartItems.objects.filter(cart__user=self.user)
    #     price = []
    #     for cart_item in cart_items:
    #         price.append(cart_item.product.price)
    #         if cart_item.color_variant:
    #             color_variant_price = cart_item.color_variant.price

    #             price.append(color_variant_price)

    #         if cart_item.size_variant:
    #             size_variant_price = cart_item.size_variant.price
    #             price.append(size_variant_price)
    #         total_price = sum(price)

    #     if total_price <= 0:
    #         total_price = 0

    #     return round(total_price + 18, 2)

    def get_cart_total(self):
        cart_items = CartItems.objects.filter(cart__user=self.user)
        price = []
        
        for cart_item in cart_items:
            price.append(cart_item.product.price)
            
            if cart_item.color_variant:
                color_variant_price = cart_item.color_variant.price
                price.append(color_variant_price)

            if cart_item.size_variant:
                size_variant_price = cart_item.size_variant.price
                price.append(size_variant_price)

        total_price = sum(price)
        
        if total_price <= 0:
            total_price = 0
            return 0
        
        # Add the fixed amount and round to 2 decimal places
        return round(total_price + 18, 2)




class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    color_variant = models.ForeignKey(ColorVariant,on_delete=models.SET_NULL,null=True,blank=True)
    size_variant = models.ForeignKey(SizeVariant,on_delete=models.SET_NULL,null=True,blank=True)


    def get_product_price(self):
        price = [self.product.price]

        if self.color_variant:
            color_variant_price = self.color_variant.price
            price.append(color_variant_price)

        if self.size_variant:
            size_variant_price = self.size_variant.price
            price.append(size_variant_price)
        return sum(price)

