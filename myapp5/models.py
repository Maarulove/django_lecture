from django.db import models

# Create your models here.


class Cattegory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    cattegory = models.ForeignKey(Cattegory, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=2)

    def __str__(self) -> str:
        return self.name
    
    @property
    def total_quantity(self):
        return sum(product.quantity for product in Product.objects.all())