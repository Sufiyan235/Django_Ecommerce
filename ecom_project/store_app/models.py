from django.db import models

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
    


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    product_image = models.ImageField(upload_to="Product_Images")
    product_slug = models.SlugField(max_length=50)
    # description=models.TextField(max_length=300,blank=True)
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product_Images')

    def __str__(self):
        return f"{self.product.product_name}"
    
class AvailableDesign(models.Model):
    available_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Product_Images',null=True,blank=True)




class ProductVariation(models.Model):
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)  # e.g., 'Size' or 'Color'

    def __str__(self):
        return f"{self.product.product_name} - {self.name}"

class ProductOption(models.Model):
    variation = models.ForeignKey(ProductVariation, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., 'Small', 'Medium', 'Red', 'Blue'
    image = models.ImageField(upload_to="Variation Images")
    additional_price = models.FloatField(default=0.0)  # Optional: additional cost for the option

    def __str__(self):
        return f"{self.variation.product.product_name} - {self.variation.name} - {self.name}"   



