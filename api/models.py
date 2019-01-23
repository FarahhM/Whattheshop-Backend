from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(null=True, blank=True) 

    def __str__(self):
        return self.name
        