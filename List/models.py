from django.db import models    

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Supermarket(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class HistoricalPrice(models.Model):
    price = models.FloatField()
    promoTag = models.BooleanField()
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name + " - " + self.supermarket.name + " - " + str(self.price)
    
class List(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ProductsList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.list.name + " - " + self.product.name

