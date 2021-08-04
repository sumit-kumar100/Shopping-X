from django.db import models
from Eshop.models import Product

# Trending Product
class DealOfDay(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)  

    def __str__(self):
        return self.product.title  

class TrendingProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


class MensTopWear(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 

    def __str__(self):
        return self.product.title 


class WomensTopWear(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)    

    def __str__(self):
        return self.product.title