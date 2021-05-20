from django.db import models

# Create your models here.
class Stock(models.Model):
    available = models.IntegerField()
    
    def __str__(self):
        return str(self.available)

class Product(models.Model):
    product_name = models.CharField(max_length=120)
    description = models.TextField(max_length=220)
    price = models.IntegerField()
    stock = models.ForeignKey(Stock,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
    

class Category(models.Model):
    title = models.CharField(max_length=120)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



