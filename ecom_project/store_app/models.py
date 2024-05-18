from django.db import models

# Create your models here.


class Category(models.Model):
    category_slug = models.SlugField(max_length=50)
    category_name = models.CharField(max_length=100)
    category_desc =models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='categories_image',null=True,blank=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_image = models.ImageField(upload_to="Product_Images")
    product_slug = models.SlugField(max_length=50)
    description=models.TextField(max_length=300,blank=True)
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
